from dataclasses import dataclass

from fastapi import FastAPI,Query
from typing import Optional
from datetime import date
from pydantic import BaseModel

from app.bookings.router import router as booking_router
from app.users.router import router_auth, router_users

app = FastAPI()

app.include_router(router_auth)
app.include_router(router_users)
app.include_router(booking_router)


