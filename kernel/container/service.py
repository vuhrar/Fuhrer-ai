from dataclasses import dataclass
from typing import Any
from typing import Callable

from .lifetime import ServiceLifetime


@dataclass(slots=True)
class ServiceDescriptor:

    key: str

    implementation: Callable[..., Any]

    lifetime: ServiceLifetime

    instance: Any | None = None
