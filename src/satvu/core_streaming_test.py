"""Tests for SDKClient streaming download functionality."""

from pathlib import Path
from tempfile import NamedTemporaryFile
from unittest.mock import MagicMock, patch

import pytest

from satvu.core import REQUEST_ID_HEADER, DownloadResult, SDKClient
from satvu.http.errors import NetworkError, ReadTimeoutError
from satvu.result import Err, Ok


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


def _ready_response(chunks=(b"zipdata",)):
    """Build a mock 'download ready' response that streams the given chunks."""
    response = MagicMock()
    response.status_code = 200
    response.headers = {"Content-Length": str(sum(len(c) for c in chunks))}
    response.iter_bytes.return_value = list(chunks)
    return response


def _accepted_response(retry_after: str | None = "1"):
    """Build a mock 202 Accepted response with an optional Retry-After header."""
    response = MagicMock()
    response.status_code = 202
    response.headers = {"Retry-After": retry_after} if retry_after is not None else {}
    return response


class TestStreamWhenReady:
    """Tests for SDKClient.stream_when_ready() polling + request-id tracking."""

    def test_ready_immediately_streams_file(self, sdk_client, temp_file):
        """A response that is ready right away is streamed without polling."""
        with (
            patch.object(
                sdk_client, "_execute_request", return_value=Ok(_ready_response())
            ) as mock_exec,
            patch("satvu.core.time.sleep") as mock_sleep,
        ):
            result = sdk_client.stream_when_ready("get", "/dl", temp_file)

        assert result.is_ok()
        outcome = result.unwrap()
        assert isinstance(outcome, DownloadResult)
        assert outcome.path == temp_file
        assert outcome.attempts == 1
        assert temp_file.read_bytes() == b"zipdata"
        mock_sleep.assert_not_called()
        assert mock_exec.call_count == 1

    def test_polls_202_then_succeeds(self, sdk_client, temp_file):
        """202 responses are polled until a ready response arrives."""
        responses = [
            Ok(_accepted_response("1")),
            Ok(_accepted_response("1")),
            Ok(_ready_response()),
        ]
        with (
            patch.object(
                sdk_client, "_execute_request", side_effect=responses
            ) as mock_exec,
            patch("satvu.core.time.sleep") as mock_sleep,
        ):
            result = sdk_client.stream_when_ready("get", "/dl", temp_file)

        assert result.is_ok()
        assert result.unwrap().attempts == 3
        assert mock_exec.call_count == 3
        assert mock_sleep.call_count == 2

    def test_same_request_id_on_every_attempt(self, sdk_client, temp_file):
        """The same X-Request-Id header is sent on the initial call and retries."""
        responses = [Ok(_accepted_response("1")), Ok(_ready_response())]
        with (
            patch.object(
                sdk_client, "_execute_request", side_effect=responses
            ) as mock_exec,
            patch("satvu.core.time.sleep"),
        ):
            result = sdk_client.stream_when_ready("get", "/dl", temp_file)

        sent_ids = [
            call.kwargs["headers"][REQUEST_ID_HEADER]
            for call in mock_exec.call_args_list
        ]
        assert len(sent_ids) == 2
        assert sent_ids[0] == sent_ids[1]
        assert sent_ids[0] == result.unwrap().request_id

    def test_caller_supplied_request_id_is_used(self, sdk_client, temp_file):
        """A caller-supplied request_id is propagated and returned unchanged."""
        with (
            patch.object(
                sdk_client, "_execute_request", return_value=Ok(_ready_response())
            ) as mock_exec,
            patch("satvu.core.time.sleep"),
        ):
            result = sdk_client.stream_when_ready(
                "get", "/dl", temp_file, request_id="my-bi-id"
            )

        assert result.unwrap().request_id == "my-bi-id"
        header = mock_exec.call_args_list[0].kwargs["headers"][REQUEST_ID_HEADER]
        assert header == "my-bi-id"

    def test_caller_headers_not_mutated(self, sdk_client, temp_file):
        """The caller's headers dict is never mutated by request-id injection."""
        caller_headers = {"X-Custom": "value"}
        with (
            patch.object(
                sdk_client, "_execute_request", return_value=Ok(_ready_response())
            ),
            patch("satvu.core.time.sleep"),
        ):
            sdk_client.stream_when_ready(
                "get", "/dl", temp_file, headers=caller_headers
            )

        assert caller_headers == {"X-Custom": "value"}

    def test_on_event_fires_expected_phases(self, sdk_client, temp_file):
        """on_event receives started -> polling -> completed with the same id."""
        responses = [Ok(_accepted_response("1")), Ok(_ready_response())]
        events = []
        with (
            patch.object(sdk_client, "_execute_request", side_effect=responses),
            patch("satvu.core.time.sleep"),
        ):
            result = sdk_client.stream_when_ready(
                "get", "/dl", temp_file, on_event=events.append
            )

        phases = [e.phase for e in events]
        assert phases == ["started", "polling", "completed"]
        request_id = result.unwrap().request_id
        assert all(e.request_id == request_id for e in events)

    def test_budget_exhausted_returns_err_and_writes_no_file(self, sdk_client):
        """A perpetually-202 download errors out without writing a file."""
        with NamedTemporaryFile(delete=True) as f:
            output_path = Path(f.name)
        # File is now deleted; assert stream_when_ready does not recreate it.
        assert not output_path.exists()

        events = []
        with (
            patch.object(
                sdk_client,
                "_execute_request",
                return_value=Ok(_accepted_response("10")),
            ),
            patch("satvu.core.time.sleep") as mock_sleep,
        ):
            result = sdk_client.stream_when_ready(
                "get",
                "/dl",
                output_path,
                max_wait_seconds=5.0,
                on_event=events.append,
            )

        assert result.is_err()
        assert isinstance(result.error(), ReadTimeoutError)
        assert not output_path.exists()
        # Never slept because the first 10s poll already exceeds the 5s budget.
        mock_sleep.assert_not_called()
        assert events[-1].phase == "failed"

    def test_transport_error_propagates(self, sdk_client, temp_file):
        """A transport error is returned as Err and emits a failed event."""
        error = NetworkError("connection refused", url="/dl")
        events = []
        with (
            patch.object(sdk_client, "_execute_request", return_value=Err(error)),
            patch("satvu.core.time.sleep"),
        ):
            result = sdk_client.stream_when_ready(
                "get", "/dl", temp_file, on_event=events.append
            )

        assert result.is_err()
        assert result.error() is error
        assert events[-1].phase == "failed"

    def test_retry_after_header_is_honored(self, sdk_client, temp_file):
        """The server's Retry-After value drives the sleep duration."""
        responses = [Ok(_accepted_response("7")), Ok(_ready_response())]
        with (
            patch.object(sdk_client, "_execute_request", side_effect=responses),
            patch("satvu.core.time.sleep") as mock_sleep,
        ):
            sdk_client.stream_when_ready("get", "/dl", temp_file)

        mock_sleep.assert_called_once_with(7.0)

    def test_poll_interval_overrides_retry_after(self, sdk_client, temp_file):
        """An explicit poll_interval takes precedence over Retry-After."""
        responses = [Ok(_accepted_response("30")), Ok(_ready_response())]
        with (
            patch.object(sdk_client, "_execute_request", side_effect=responses),
            patch("satvu.core.time.sleep") as mock_sleep,
        ):
            sdk_client.stream_when_ready("get", "/dl", temp_file, poll_interval=2.0)

        mock_sleep.assert_called_once_with(2.0)

    def test_missing_retry_after_falls_back_to_default(self, sdk_client, temp_file):
        """A 202 without Retry-After polls using the default interval."""
        responses = [Ok(_accepted_response(retry_after=None)), Ok(_ready_response())]
        with (
            patch.object(sdk_client, "_execute_request", side_effect=responses),
            patch("satvu.core.time.sleep") as mock_sleep,
        ):
            sdk_client.stream_when_ready("get", "/dl", temp_file)

        # DEFAULT_POLL_INTERVAL_SECONDS == 5.0
        mock_sleep.assert_called_once_with(5.0)

    def test_follow_redirects_always_enabled(self, sdk_client, temp_file):
        """Requests are issued with follow_redirects so 307 -> content resolves."""
        with (
            patch.object(
                sdk_client, "_execute_request", return_value=Ok(_ready_response())
            ) as mock_exec,
            patch("satvu.core.time.sleep"),
        ):
            sdk_client.stream_when_ready("get", "/dl", temp_file)

        assert mock_exec.call_args_list[0].kwargs["follow_redirects"] is True
