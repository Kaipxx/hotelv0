from fastapi import APIRouter

from app.bookings.dao import BookingDAO

from app.users.dependencies import get_current_user
from app.users.models import Users
from app.bookings.models import Bookings
from fastapi import Depends

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"],
)


@router.get("")
async def get_bookings(user:Users = Depends(get_current_user)):# -> list[SBooking]
    #print(user,type(user),user.email)
    #return user
    return await BookingDAO.find_all(user_id = user.id)

