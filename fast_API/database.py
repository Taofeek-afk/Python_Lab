from models import Base
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

DATABASE_URL = "sqlite+aiosqlite:///./restaurant.db"

engine =  create_async_engine(
    DATABASE_URL,
    echo=True,
    pool_pre_ping=True, # checks connections before using them.
)


async_session = async_sessionmaker( # AsyncSessionLocal, SessionLocal
    engine,
    class_=AsyncSession, # ?
    expire_on_commit=False, # after committing you can still access the object's loaded attributes without SQLAlchemy expiring them.
)


async def get_session():
    async with async_session() as session:
        yield session


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all) # Notes: line 17


# Pydantic schemas, where we'll finally handle things like email validation, 
# request validation, response serialization, and API-facing models.


# from sqlalchemy.orm import DeclarativeBase

# class Base(DeclarativeBase):
#     pass

# app/models/__init__.py:

# from app.models.base import Base
# from app.models.restaurant import Restaurant
# from app.models.menu import MenuItem
# from app.models.order import Order

# __all__ = ["Base", "Restaurant", "MenuItem", "Order"]
# from app.models import Base  # Automatically loads all models exposed in __init__.py


# app/database.py
# from app.models.base import Base
# import app.models.restaurant  
# import app.models.menu 
# import app.models.order       

# async def init_db() -> None:
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)

