from app.exceptions import DetailedHTTPException
from app.posts.constants import ErrorCode


class AuthorNotFound(DetailedHTTPException):
    status_code = 404
    detail = ErrorCode.AUTHOR_NOT_FOUND
