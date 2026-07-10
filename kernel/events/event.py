from dataclasses import dataclass
from datetime import UTC, datetime
from uuid import uuid4


@dataclass(slots=True)
class Event:

    id: str

    name: str

    payload: dict

    created_at: datetime

    @classmethod
    def create(
        cls,
        name: str,
        payload: dict,
    ):

        return cls(
            id=str(uuid4()),
            name=name,
            payload=payload,
            created_at=datetime.now(UTC),
        )
