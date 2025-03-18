from dataclasses import dataclass

from fastapi import FastAPI,Query
from typing import Optional
from datetime import date
from pydantic import BaseModel


app = FastAPI()

class SHotel(BaseModel):
    address:str
    name:str
    stars:int

@dataclass
class HotelSearchArgs():
    location: str
    date_from: date
    date_to: date
    has_spa: Optional[bool] = None,
    stars: Optional[int] = Query(None, ge=1, le=5)

@app.get("/hotels",response_model=list[SHotel])
def get_hotels(seaching_args:HotelSearchArgs):
    return seaching_args


class SBooking(BaseModel):
    room_id:int
    date_from:date
    date_to:date


@app.post("/bookings")
def add_booking(booking:SBooking):
    pass