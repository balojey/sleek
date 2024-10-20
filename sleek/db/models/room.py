from typing import Union
from datetime import datetime, timezone
from uuid import uuid4
from sqlmodel import SQLModel, Field


def generate_id() -> str:
    return str(uuid4())


def get_datetime() -> datetime:
    return datetime.now(timezone.utc)


class Room(SQLModel, table=True):
    id: str = Field(default_factory=generate_id, primary_key=True)
    name: str
    created_at: datetime = Field(default_factory=get_datetime)
    updated_at: datetime = Field(default_factory=get_datetime)
    canvas_data: Union[str, None] = None