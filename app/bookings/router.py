from fastapi import APIRouter

from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking, SNewBooking
from app.exceptions import RoomCannotBeBooked

from app.users.dependencies import get_current_user
from app.users.models import Users
from app.bookings.models import Bookings
from fastapi import Depends

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"],
)


@router.get("")
async def get_bookings(user:Users = Depends(get_current_user))-> list[SBooking]:
    #print(user,type(user),user.email)
    #return user
    return await BookingDAO.find_all(user_id = user.id)



# @router.post("", status_code=201)
# async def add_booking(
#
#     booking: SNewBooking,
#     #background_tasks: BackgroundTasks,
#     user: Users = Depends(get_current_user),
# ):
#     booking = await BookingDAO.add(
#         user.id,
#         booking.room_id,
#         booking.date_from,
#         booking.date_to,
#     )
#     if not booking:
#         raise RoomCannotBeBooked
#     # TypeAdapter и model_dump - это новинки версии Pydantic 2.0
#     booking = TypeAdapter(SNewBooking).validate_python(booking).model_dump()
#     # Celery - отдельная библиотека
#     # send_booking_confirmation_email.delay(booking, user.email)
#     # Background Tasks - встроено в FastAPI
#     # background_tasks.add_task(send_booking_confirmation_email, booking, user.email)
#     return booking


@router.post("")
async def add_booking(

    booking: SNewBooking,
    #background_tasks: BackgroundTasks,
    user: Users = Depends(get_current_user),
):
    booking = await BookingDAO.add(
        user.id,
        booking.room_id,
        booking.date_from,
        booking.date_to,
    )
    if not booking:
        raise RoomCannotBeBooked
    # # TypeAdapter и model_dump - это новинки версии Pydantic 2.0
    # booking = TypeAdapter(SNewBooking).validate_python(booking).model_dump()
    # # Celery - отдельная библиотека
    # # send_booking_confirmation_email.delay(booking, user.email)
    # # Background Tasks - встроено в FastAPI
    # # background_tasks.add_task(send_booking_confirmation_email, booking, user.email)
    # return booking


@router.delete("")
async def delete_booking(room

    #booking: SNewBooking,
    #background_tasks: BackgroundTasks,
    #user: Users = Depends(get_current_user),
):
    del_booking = await BookingDAO.delete(
        room_id = int(room))