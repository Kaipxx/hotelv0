from fastapi import APIRouter

from app.hotels.dao import HotelsDAO

#from fastapi_cache.decorator import cache


router = APIRouter(prefix="/hotels", tags=["Отели"])


# @router.get("/{location}")
# #@cache(expire=30)
# async def get_hotels_by_location_and_time(_, *, /) -> ...:
#     ...
@router.get("")
async def get_bookings_location(loc):#-> list[SBooking]:
    #print(user,type(user),user.email)
    #return user
    return await HotelsDAO.find_by_location(location = loc)