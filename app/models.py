import uuid
from enum import Enum
from typing import List
from sqlalchemy import Enum as SQLEnum, DateTime, String, Text, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID, ARRAY
from datetime import datetime

class Difficulty(Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"

class Base(DeclarativeBase):
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())

class Problem(Base):
    __tablename__ = 'problems'

    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    difficulty: Mapped[Difficulty] = mapped_column(SQLEnum(Difficulty, values_callable=lambda x: [e.value for e in x]), nullable=False)
    tags: Mapped[List[str]] = mapped_column(ARRAY(String), nullable=False, default=list)
    hints: Mapped[List[str]] = mapped_column(ARRAY(String), nullable=False, default=list)
