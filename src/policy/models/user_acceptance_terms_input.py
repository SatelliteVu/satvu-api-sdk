from pydantic import BaseModel


class UserAcceptanceTermsInput(BaseModel):
    """
    Attributes:
        accepted (bool): Terms and Conditions have been accepted
        token (str): User access token
    """

    accepted: bool
    token: str
