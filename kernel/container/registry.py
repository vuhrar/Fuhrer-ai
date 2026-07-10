from typing import Any


class ServiceRegistry:
    """
    Stores registered services.
    """

    def __init__(self) -> None:
        self._services: dict[str, Any] = {}

    def register(
        self,
        key: str,
        service: Any,
    ) -> None:

        if key in self._services:
            raise ValueError(f"Service '{key}' already exists.")

        self._services[key] = service

    def resolve(
        self,
        key: str,
    ) -> Any:

        if key not in self._services:
            raise KeyError(f"Unknown service '{key}'.")

        return self._services[key]

    def contains(
        self,
        key: str,
    ) -> bool:

        return key in self._services

    def clear(self) -> None:
        self._services.clear()

    @property
    def services(self) -> dict[str, Any]:
        return self._services
