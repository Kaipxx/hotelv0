from fastapi import APIRouter

#from fastapi_cache.decorator import cache


router = APIRouter(prefix="/hotels", tags=["Отели"])


@router.get("/{location}")
#@cache(expire=30)
async def get_hotels_by_location_and_time(_, *, /) -> ...:
    ...
