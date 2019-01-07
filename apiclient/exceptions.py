class ApiClientException(Exception):
    """Base class for all apiclient exceptions."""


class StorageException(ApiClientException):
    """Error raised when there's problems with storage."""
    pass
