from abc import ABC, abstractmethod
from typing import Any


class Provider(ABC):
    """
    Base provider interface.
    """

    @abstractmethod
    def build(self) -> Any:
        raise NotImplementedError
