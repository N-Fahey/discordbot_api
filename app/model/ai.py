from datetime import datetime
from sqlalchemy import Integer, BigInteger, String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncSession

from .main import Base

class AIMessage(Base):
    __tablename__ = 'bot_ai_messages'
    id: Mapped[int] = mapped_column('id', Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id: Mapped[int] = mapped_column('user_id', ForeignKey('bot_users.id'), nullable=True)
    conversation_id: Mapped[int] = mapped_column('conversation_id', BigInteger, nullable=False)
    message_id: Mapped[int] = mapped_column('message_id', BigInteger, nullable=False, unique=True)
    text: Mapped[str] = mapped_column('text', String(2000), nullable=False)

    @classmethod
    async def add_message(cls, session: AsyncSession, user_id:int, conversation_id:int, message_id:int, text:str):
        new_message = AIMessage(user_id = user_id, conversation_id=conversation_id, message_id=message_id, text=text)
        session.add(new_message)
        await session.flush()

        return new_message


class AIUsage(Base):
    __tablename__ = 'bot_ai_usage'
    id: Mapped[int] = mapped_column('id', Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id: Mapped[int] = mapped_column('user_id', ForeignKey('bot_users.id'))
    type: Mapped[str] = mapped_column('type', String(16), nullable=False)
    tokens: Mapped[int] = mapped_column('tokens', Integer, nullable=False)
    timestamp: Mapped[datetime] = mapped_column('timestamp', DateTime, nullable=False)