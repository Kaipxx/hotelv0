from fastapi import APIRouter
from sqlalchemy import select
from app.database import async_session_maker
from app.users.models import Users


router = APIRouter(
    prefix="/users",
    tags=["Бронирования"],
)


@router.get("")
async def get_users():
    async with async_session_maker() as session:
        query = select(Users) # SELECT * FROM bookings
        result = await session.execute(query)
        return result.mappings().all()

