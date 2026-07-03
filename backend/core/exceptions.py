from fastapi import HTTPException, status


class FuhrerException(Exception):
    """Base application exception."""


class ConfigurationError(FuhrerException):
    pass


class AuthenticationError(FuhrerException):
    pass


class AuthorizationError(FuhrerException):
    pass


class ValidationError(FuhrerException):
    pass


class DatabaseError(FuhrerException):
    pass


class AIEngineError(FuhrerException):
    pass


class PluginError(FuhrerException):
    pass


def unauthorized(detail: str = "Unauthorized") -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=detail,
    )


def forbidden(detail: str = "Forbidden") -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail=detail,
    )


def not_found(detail: str = "Resource not found") -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=detail,
    )
