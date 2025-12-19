"""Tests for SDKClient streaming download functionality."""

from pathlib import Path
from tempfile import NamedTemporaryFile
from unittest.mock import MagicMock

import pytest

from satvu.core import SDKClient


class ConcreteSDKClient(SDKClient):
    """Concrete implementation for testing abstract SDKClient."""

    base_path = "/test"


@pytest.fixture
def sdk_client():
    """Create a basic SDKClient instance for testing."""
    return ConcreteSDKClient(env=None)


@pytest.fixture
def mock_response():
    """Create a mock HTTP response with iter_bytes support."""
    response = MagicMock()
    response.status_code = 200
    response.headers = {"Content-Length": "1024"}
    return response


@pytest.fixture
def temp_file():
    """Create a temporary file for testing."""
    with NamedTemporaryFile(delete=False) as f:
        yield Path(f.name)
    # Cleanup
    Path(f.name).unlink(missing_ok=True)


class TestStreamToFile:
    """Tests for SDKClient.stream_to_file() method."""

    @pytest.mark.parametrize(
        "chunks,expected_content",
        [
            ([b"chunk1", b"chunk2", b"chunk3"], b"chunk1chunk2chunk3"),
            ([b"test", b"data"], b"testdata"),
            ([b"hello", b" ", b"world", b"!!!!"], b"hello world!!!!"),
            ([b"no", b"length"], b"nolength"),
            ([b"data"], b"data"),
            ([], b""),  # Empty response
        ],
    )
    def test_stream_to_file_various_chunks(
        self, sdk_client, mock_response, temp_file, chunks, expected_content
    ):
        """Test streaming with various chunk patterns."""
        mock_response.iter_bytes.return_value = chunks

        result_path = sdk_client.stream_to_file(
            response=mock_response,
            output_path=temp_file,
        )

        assert result_path == temp_file
        assert temp_file.exists()
        assert temp_file.read_bytes() == expected_content

    @pytest.mark.parametrize(
        "headers,expected_total",
        [
            ({"Content-Length": "12"}, 12),
            ({"content-length": "10"}, 10),  # Case insensitive
            ({}, None),  # No Content-Length
            ({"Content-Length": "not-a-number"}, None),  # Invalid
        ],
    )
    def test_stream_to_file_content_length_handling(
        self, sdk_client, mock_response, temp_file, headers, expected_total
    ):
        """Test handling of Content-Length header in various formats."""
        mock_response.headers = headers
        mock_response.iter_bytes.return_value = [b"1234", b"5678"]

        progress_calls = []

        def progress_callback(bytes_downloaded: int, total_bytes: int | None):
            progress_calls.append((bytes_downloaded, total_bytes))

        sdk_client.stream_to_file(
            response=mock_response,
            output_path=temp_file,
            progress_callback=progress_callback,
        )

        # Verify total_bytes matches expected
        assert all(call[1] == expected_total for call in progress_calls)

    @pytest.mark.parametrize(
        "chunk_size",
        [8192, 4096, 65536, 1024],
    )
    def test_stream_to_file_chunk_sizes(
        self, sdk_client, mock_response, temp_file, chunk_size
    ):
        """Test streaming with various chunk sizes."""
        mock_response.iter_bytes.return_value = [b"data"]

        sdk_client.stream_to_file(
            response=mock_response,
            output_path=temp_file,
            chunk_size=chunk_size,
        )

        mock_response.iter_bytes.assert_called_once_with(chunk_size=chunk_size)

    @pytest.mark.parametrize(
        "output_path_type",
        ["path", "string"],
    )
    def test_stream_to_file_path_types(
        self, sdk_client, mock_response, temp_file, output_path_type
    ):
        """Test streaming with Path object vs string path."""
        mock_response.iter_bytes.return_value = [b"test"]

        output = temp_file if output_path_type == "path" else str(temp_file)

        result_path = sdk_client.stream_to_file(
            response=mock_response,
            output_path=output,
        )

        assert isinstance(result_path, Path)
        assert result_path == temp_file
        assert temp_file.read_bytes() == b"test"

    def test_stream_to_file_with_progress_callback(
        self, sdk_client, mock_response, temp_file
    ):
        """Test streaming with progress callback."""
        mock_response.headers = {"Content-Length": "12"}
        mock_response.iter_bytes.return_value = [b"1234", b"5678", b"90AB"]

        progress_calls = []

        def progress_callback(bytes_downloaded: int, total_bytes: int | None):
            progress_calls.append((bytes_downloaded, total_bytes))

        result_path = sdk_client.stream_to_file(
            response=mock_response,
            output_path=temp_file,
            progress_callback=progress_callback,
        )

        assert result_path == temp_file
        assert len(progress_calls) == 3
        assert progress_calls[0] == (4, 12)
        assert progress_calls[1] == (8, 12)
        assert progress_calls[2] == (12, 12)

    def test_stream_to_file_large_file(self, sdk_client, mock_response, temp_file):
        """Test streaming with large file (many chunks)."""
        chunks = [b"X" * 1024 for _ in range(100)]
        mock_response.headers = {"Content-Length": str(100 * 1024)}
        mock_response.iter_bytes.return_value = chunks

        result_path = sdk_client.stream_to_file(
            response=mock_response,
            output_path=temp_file,
        )

        assert result_path == temp_file
        assert temp_file.stat().st_size == 100 * 1024

    def test_stream_to_file_overwrites_existing(
        self, sdk_client, mock_response, temp_file
    ):
        """Test that streaming overwrites existing file."""
        temp_file.write_text("old content")
        mock_response.iter_bytes.return_value = [b"new content"]

        sdk_client.stream_to_file(
            response=mock_response,
            output_path=temp_file,
        )

        assert temp_file.read_bytes() == b"new content"

    def test_stream_to_file_creates_parent_directories(self, sdk_client, mock_response):
        """Test that streaming requires parent directories to exist."""
        import tempfile

        with tempfile.TemporaryDirectory() as tmpdir:
            nested_path = Path(tmpdir) / "subdir" / "nested" / "file.bin"
            mock_response.iter_bytes.return_value = [b"test"]

            with pytest.raises(FileNotFoundError):
                sdk_client.stream_to_file(
                    response=mock_response,
                    output_path=nested_path,
                )

    def test_stream_to_file_binary_data(self, sdk_client, mock_response, temp_file):
        """Test streaming with binary (non-text) data."""
        binary_chunks = [
            b"\x00\x01\x02\x03",
            b"\xff\xfe\xfd\xfc",
            b"\x80\x90\xa0\xb0",
        ]
        mock_response.iter_bytes.return_value = binary_chunks

        result_path = sdk_client.stream_to_file(
            response=mock_response,
            output_path=temp_file,
        )

        assert result_path == temp_file
        assert (
            temp_file.read_bytes()
            == b"\x00\x01\x02\x03\xff\xfe\xfd\xfc\x80\x90\xa0\xb0"
        )


class TestStreamToFileErrorHandling:
    """Tests for error handling in stream_to_file()."""

    @pytest.mark.parametrize(
        "exception_class,exception_msg",
        [
            (RuntimeError, "Network error during streaming"),
            (IOError, "Disk write error"),
        ],
    )
    def test_stream_to_file_with_exception_in_iter_bytes(
        self, sdk_client, mock_response, temp_file, exception_class, exception_msg
    ):
        """Test handling when iter_bytes raises various exceptions."""

        def failing_iter():
            yield b"start"
            raise exception_class(exception_msg)

        mock_response.iter_bytes.return_value = failing_iter()

        with pytest.raises(exception_class, match=exception_msg):
            sdk_client.stream_to_file(
                response=mock_response,
                output_path=temp_file,
            )

    def test_stream_to_file_with_progress_callback_exception(
        self, sdk_client, mock_response, temp_file
    ):
        """Test that exceptions in progress callback are propagated."""
        mock_response.iter_bytes.return_value = [b"data"]

        def failing_callback(bytes_downloaded: int, total_bytes: int | None):
            raise ValueError("Callback error")

        with pytest.raises(ValueError, match="Callback error"):
            sdk_client.stream_to_file(
                response=mock_response,
                output_path=temp_file,
                progress_callback=failing_callback,
            )
