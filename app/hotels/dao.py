from sqlalchemy import select

from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.hotels.models import Hotels


class HotelsDAO(BaseDAO):
    model = Hotels


    @classmethod
    async def find_by_location(cls, location):
        async with async_session_maker() as session:
            stmt = select(cls.model).where(cls.model.location.ilike(f"%{location}%"))
            result = await session.execute(stmt)
            return result.scalars().all()


    """
WITH findword AS(
SELECT * FROM hotels
WHERE hotels.location LIKE '%Алтай%'
)
SELECT * FROM findword
    """

    # @classmethod
    # async def get_hotels(cls,  **location):
    #     async with async_session_maker() as session:
    #         result = await session.execute(
    #             select(Hotels).where(Hotels.location.ilike('%location%'))
    #         )
    #         return result.mappings().all()