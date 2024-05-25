from fastapi import status

from app.exceptions import DetailedHTTPException
from app.users.constants import ErrorCode


class EmailAlreadyExists(DetailedHTTPException):
    STATUS_CODE = status.HTTP_400_BAD_REQUEST
    DETAIL = ErrorCode.EMAIL_ALREADY_EXISTS
