from abc import ABC
from abc import abstractmethod
from typing import Any


class Provider(ABC):
    """
    Base provider interface.
    """

    @abstractmethod
    def build(self) -> Any:
        raise NotImplementedError
