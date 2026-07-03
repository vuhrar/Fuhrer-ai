from typing import Any

from .registry import ServiceRegistry


class Container:
    """
    Application service container.
    """

    def __init__(self) -> None:

        self._registry = ServiceRegistry()

    def singleton(
        self,
        key: str,
        service: Any,
    ) -> None:

        self._registry.register(
            key,
            service,
        )

    def resolve(
        self,
        key: str,
    ) -> Any:

        return self._registry.resolve(key)

    def exists(
        self,
        key: str,
    ) -> bool:

        return self._registry.contains(key)

    def clear(self) -> None:

        self._registry.clear()


container = Container()
