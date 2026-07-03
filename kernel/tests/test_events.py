import pytest

from kernel.events import Event
from kernel.events import EventBus
from kernel.events import EventHandler


class DemoHandler(EventHandler):

    def __init__(self):

        self.called = False

    async def handle(self, event):

        self.called = True


@pytest.mark.asyncio
async def test_event_bus():

    bus = EventBus()

    handler = DemoHandler()

    bus.subscribe(
        "startup",
        handler,
    )

    await bus.publish(
        Event.create(
            "startup",
            {},
        )
    )

    assert handler.called
