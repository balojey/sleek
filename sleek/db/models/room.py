from datetime import datetime
from uuid import uuid4
from sqlmodel import SQLModel, Field


class Room(SQLModel, table=True):
    id: str = Field(default_factory=str(uuid4()))
    created_at: str = Field(default_factory=datetime.now().strftime())
    updated_at: str = Field(default_factory=datetime.now().strftime())