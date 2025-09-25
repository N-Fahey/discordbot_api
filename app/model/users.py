from __future__ import annotations

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
    balance: Mapped[int] = mapped_column('balance', Integer, nullable=False, default=0)
    last_dole: Mapped[Optional[datetime]] = mapped_column('last_dole', DateTime, nullable=True)

    @classmethod
    async def check_user_exists(cls, session: AsyncSession, uid:int | None = None, username:str | None = None):
        if not uid and not username:
            return None

        stmt = select(User).where((User.uid == uid) | (User.username == username))
        existing_user = await session.scalar(stmt)
        
        return bool(existing_user)

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
    
    @classmethod
    async def get_users_with_balance(cls, session: AsyncSession, user_count:int | None = None):
        stmt = select(User).where(User.balance > 0).order_by(User.balance.desc()).limit(user_count)
        user_stream = await session.stream_scalars(stmt)

        async for user in user_stream:
            yield user
    
    @classmethod
    async def get_all_users(cls, session: AsyncSession):
        stmt = select(User)
        user_stream = await session.stream_scalars(stmt)

        async for user in user_stream:
            yield user
    
    @staticmethod
    async def transfer(session: AsyncSession, from_user:User, to_user:User, amount:int):
        if from_user.balance < amount:
            raise ValueError("Amount to withdraw greater than balance.")

        from_user.balance -= amount
        to_user.balance += amount
        await session.flush()
    
    async def deposit(self, session: AsyncSession, amount: int):
        self.balance += amount
        await session.flush()
    
    async def withdraw(self, session: AsyncSession, amount: int):
        if self.balance < amount:
            raise ValueError("Amount to withdraw greater than balance.")
        self.balance -= amount
        await session.flush()
    
    async def update_user(self, session: AsyncSession, username:str | None, display_name:str | None):
        if username:
            self.username = username
        if display_name:
            self.display_name = display_name
        
        await session.flush()
    
    async def update_dole(self, session: AsyncSession):
        self.last_dole = datetime.now()

        await session.flush()