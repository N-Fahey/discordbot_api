from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from dotenv import load_dotenv
from os import getenv

load_dotenv()

env_dict = {
    'DB_USER': getenv('DB_USER'),
    'DB_PASSWORD': getenv('DB_PASSWORD'),
    'DB_HOST': getenv('DB_HOST'),
    'DB_PORT': getenv('DB_PORT'),
    'DB_NAME': getenv('DB_NAME'),
}

missing_envs = [k for k,v in env_dict.items() if v is None]

if missing_envs:
    raise EnvironmentError(f"Missing environment variables: [{', '.join(missing_envs)}]")

db_connstr = f'mysql+aiomysql://{env_dict['DB_USER']}:{env_dict['DB_PASSWORD']}@{env_dict['DB_HOST']}:{env_dict['DB_PORT']}/{env_dict['DB_NAME']}?charset=utf8mb4'

engine = create_async_engine(db_connstr, echo=False, pool_recycle = 3600)

DBSession = async_sessionmaker(bind=engine)

async def get_session():
    yield DBSession

DBSessionDep = Annotated[async_sessionmaker, Depends(get_session)]