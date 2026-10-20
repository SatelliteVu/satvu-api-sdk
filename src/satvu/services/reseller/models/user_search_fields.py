from enum import StrEnum


class UserSearchFields(StrEnum):
    COMPANY_NAME = "company_name"
    USER_EMAIL = "user_email"
    USER_ID = "user_id"
    USER_NAME = "user_name"

    def __str__(self) -> str:
        return str(self.value)
