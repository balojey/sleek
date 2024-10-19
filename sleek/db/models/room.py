from datetime import datetime
from uuid import uuid4
from sqlmodel import SQLModel, Field


class Room(SQLModel, table=True):
    id: str = Field(default_factory=uuid4, primary_key=True)
    created_at: str = Field(default_factory=datetime.now)
    updated_at: str = Field(default_factory=datetime.now)