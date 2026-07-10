import asyncio

from kernel.events import Event, EventBus, EventHandler


class DemoHandler(EventHandler):
    def __init__(self):
        self.called = False

    async def handle(self, event):
        self.called = True


def test_event_bus():
    async def run_event_bus() -> None:
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

    asyncio.run(run_event_bus())
