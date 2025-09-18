from typing import Optional
from datetime import datetime
from sqlalchemy import Integer, BigInteger, String, DateTime, select
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncSession

from .main import Base

class User(Base):
    __tablename__ = 'bot_users'
    id: Mapped[int] = mapped_column('id', Integer, primary_key=True, autoincrement=True, nullable=False)
    uid: Mapped[int] = mapped_column('uid', BigInteger, unique=True, nullable=False)
    username: Mapped[str] = mapped_column('username', String(64), unique=True, nullable=False)
    display_name: Mapped[str] = mapped_column('display_name', String(64), nullable=False)
    bank: Mapped[int] = mapped_column('bank', Integer, nullable=False, default=0)
    last_dole: Mapped[Optional[datetime]] = mapped_column('last_dole', DateTime, nullable=True)

    @classmethod
    async def create_user(cls, session: AsyncSession, uid:int, username:str, display_name:str):
        new_user = User(uid=uid, username=username, display_name=display_name)
        session.add(new_user)
        await session.flush()

        return new_user
    
    @classmethod
    async def get_user_by_uid(cls, session: AsyncSession, uid:int):
        stmt = select(User).where(User.uid == uid)
        user = await session.scalar(stmt)

        return user