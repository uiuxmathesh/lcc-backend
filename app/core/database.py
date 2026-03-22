from fastapi import FastAPI
from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from .settings import settings

engine=None
SessionLocal=None

def init_db(database_dsn: str):
    global engine, SessionLocal

    engine = create_async_engine(
        url=database_dsn,
        echo=True,
        pool_size=10,
        max_overflow=20
    )

    SessionLocal = async_sessionmaker(
        bind=engine,
        expire_on_commit=False
    )


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db(settings.postgres_url)
    app.state.engine = engine
    app.state.SessionLocal = SessionLocal
    print("DB initialized")

    yield

    if engine:
        await engine.dispose()
    print("DB closed")