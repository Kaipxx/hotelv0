from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
#from config import settings
from app.config import settings

#DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# создаём движок. для передачи url в алхимию
engine = create_async_engine(settings.DATABASE_URL, future=True)
#создаём сессии(транзакций)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

#в base аккумулируются данные для создания таблиц
class Base(DeclarativeBase):
    pass
