from typing import Any


class ServiceContainer:

    def __init__(self) -> None:
        self._services: dict[str, Any] = {}

    def register(
        self,
        name: str,
        service: Any,
    ) -> None:

        self._services[name] = service

    def resolve(
        self,
        name: str,
    ) -> Any:

        if name not in self._services:
            raise KeyError(f"Service '{name}' not found.")

        return self._services[name]


container = ServiceContainer()
