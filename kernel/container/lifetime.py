from enum import StrEnum


class ServiceLifetime(StrEnum):

    SINGLETON = "singleton"

    TRANSIENT = "transient"

    SCOPED = "scoped"
