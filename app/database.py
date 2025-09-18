from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from dotenv import load_dotenv
from os import getenv

load_dotenv()
db_connstr = f'mysql+aiomysql://{getenv('DB_USER')}:{getenv('DB_PASSWORD')}@{getenv('DB_HOST')}:{getenv('DB_PORT')}/{getenv('DB_NAME')}?charset=utf8mb4'

engine = create_async_engine(db_connstr, echo=False, pool_recycle = 3600)

DBSession = async_sessionmaker(bind=engine)

async def get_session():
    yield DBSession

DBSessionDep = Annotated[async_sessionmaker, Depends(get_session)]