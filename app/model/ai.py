from datetime import datetime
from sqlalchemy import Integer, BigInteger, String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .main import Base

class AIMessage(Base):
    __tablename__ = 'bot_ai_messages'
    id: Mapped[int] = mapped_column('id', Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id: Mapped[int] = mapped_column('user_id', ForeignKey('bot_users.id'))
    conversation_id: Mapped[int] = mapped_column('conversation_id', BigInteger, nullable=False)
    message_id: Mapped[int] = mapped_column('message_id', BigInteger, nullable=False)
    text: Mapped[str] = mapped_column('text', String(2000), nullable=False)

class AIUsage(Base):
    __tablename__ = 'bot_ai_usage'
    id: Mapped[int] = mapped_column('id', Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id: Mapped[int] = mapped_column('user_id', ForeignKey('bot_users.id'))
    type: Mapped[str] = mapped_column('type', String(16), nullable=False)
    tokens: Mapped[int] = mapped_column('tokens', Integer, nullable=False)
    timestamp: Mapped[datetime] = mapped_column('timestamp', DateTime, nullable=False)