from fastapi import HTTPException, status


class FuhrerError(Exception):
    """Base application exception."""


FuhrerException = FuhrerError


class ConfigurationError(FuhrerError):
    pass


class AuthenticationError(FuhrerError):
    pass


class AuthorizationError(FuhrerError):
    pass


class ValidationError(FuhrerError):
    pass


class DatabaseError(FuhrerError):
    pass


class AIEngineError(FuhrerError):
    pass


class PluginError(FuhrerError):
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
