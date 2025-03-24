from fastapi import APIRouter
from app.users.auth import get_password_hash
from app.users.dao import UserDAO
from app.users.schemas import SUserAuth


router = APIRouter(
    prefix="/auth",
    tags=["Auth и Пользователи"],
)

@router_auth.post("/register", status_code=201)
async def register_user(user_data: SUserAuth):
    existing_user = await UserDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise UserAlreadyExistsException
    hashed_password = get_password_hash(user_data.password)
    new_user = await UserDAO.add(email=user_data.email, hashed_password=hashed_password)



