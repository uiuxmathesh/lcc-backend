from typing  import AsyncGenerator, Annotated
from fastapi import FastAPI, APIRouter, Depends, Request
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from .core.database import lifespan

router = APIRouter()

app = FastAPI(
    lifespan=lifespan
)

async def get_db(request: Request) -> AsyncGenerator[AsyncSession, None]:
    SessionLocal = request.app.state.SessionLocal
    async with SessionLocal() as session:
        yield session

DBSession = Annotated[AsyncSession, Depends(get_db)]

@router.get("/")
async def health(session:DBSession):
    await session.execute(text("SELECT 1"))
    return {"message": "health check successful"}


app.include_router(router)