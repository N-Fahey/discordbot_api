from datetime import datetime
from sqlalchemy import Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .main import Base

class Game(Base):
    __tablename__ = 'bot_games'
    id: Mapped[int] = mapped_column('id', Integer, primary_key=True, autoincrement=True, nullable=False)
    name: Mapped[str] = mapped_column('name', String(100), unique=True, nullable=False)

class Score(Base):
    __tablename__ = 'bot_scores'
    id: Mapped[int] = mapped_column('id', Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id: Mapped[int] = mapped_column('user_id', ForeignKey('bot_users.id'))
    game_id: Mapped[int] = mapped_column('game_id', ForeignKey('bot_games.id'))
    timestamp: Mapped[datetime] = mapped_column('timestamp', DateTime, nullable=False)