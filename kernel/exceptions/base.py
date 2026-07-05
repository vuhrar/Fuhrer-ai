class FuhrerError(Exception):
    """
    Base exception for the platform.
    """


class ConfigurationError(FuhrerError):
    pass


class DependencyError(FuhrerError):
    pass


class SecurityError(FuhrerError):
    pass


class DatabaseError(FuhrerError):
    pass


class AIProviderError(FuhrerError):
    pass


class PluginError(FuhrerError):
    pass
