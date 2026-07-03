from abc import ABC
from abc import abstractmethod

from .event import Event


class EventHandler(ABC):

    @abstractmethod
    async def handle(
        self,
        event: Event,
    ) -> None:
        raise NotImplementedError
