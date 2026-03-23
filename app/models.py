import uuid
from enum import Enum
from typing import List, Optional
from sqlalchemy import Column, Enum as SQLEnum, Uuid, DateTime, String, func, JSON
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime

class Difficulty(Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"

class Base(DeclarativeBase):
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, onupdate=func.now())

class Problem(Base):
    __tablename__ = 'problem'

    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    difficulty: Mapped[Difficulty] = mapped_column(SQLEnum(Difficulty), nullable=False)
    tags: Mapped[List[str]] = mapped_column(JSON, nullable=True, default=[])
    hints: Mapped[List[str]] = mapped_column(JSON, nullable=True, default=[])
