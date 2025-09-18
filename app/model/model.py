from datetime import datetime
from sqlalchemy import Integer, BigInteger, String, DateTime, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    def __repr__(self) -> str:
        columns = ", ".join(
            [f"{k}={repr(v)}" for k, v in self.__dict__.items() if not k.startswith("_")]
        )
        return f"<{self.__class__.__name__}({columns})>"

class Users(Base):
    __tablename__ = 'bot_users'
    id: Mapped[int] = mapped_column('id', Integer, primary_key=True, autoincrement=True, nullable=False)
    uid: Mapped[int] = mapped_column('uid', BigInteger, unique=True, nullable=False)
    username: Mapped[str] = mapped_column('username', String(64), unique=True, nullable=False)
    display_name: Mapped[str] = mapped_column('display_name', String(64), nullable=False)
    bank: Mapped[int] = mapped_column('bank', Integer, nullable=False, default=0)
    last_dole: Mapped[datetime] = mapped_column('last_dole', DateTime, nullable=True)

class Games(Base):
    __tablename__ = 'bot_games'
    id: Mapped[int] = mapped_column('id', Integer, primary_key=True, autoincrement=True, nullable=False)
    name: Mapped[str] = mapped_column('name', String(100), unique=True, nullable=False)

class Scores(Base):
    __tablename__ = 'bot_scores'
    id: Mapped[int] = mapped_column('id', Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id: Mapped[int] = mapped_column('user_id', ForeignKey('bot_users.id'))
    game_id: Mapped[int] = mapped_column('game_id', ForeignKey('bot_games.id'))
    timestamp: Mapped[datetime] = mapped_column('timestamp', DateTime, nullable=False)

class AIMessages(Base):
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