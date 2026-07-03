from collections import defaultdict

from .event import Event
from .handler import EventHandler


class EventBus:

    def __init__(self):

        self._handlers: dict[
            str,
            list[EventHandler],
        ] = defaultdict(list)

    def subscribe(
        self,
        event_name: str,
        handler: EventHandler,
    ) -> None:

        self._handlers[event_name].append(
            handler
        )

    async def publish(
        self,
        event: Event,
    ) -> None:

        for handler in self._handlers.get(
            event.name,
            [],
        ):

            await handler.handle(event)
