from datetime import datetime
from sqlalchemy import Integer, String, DateTime, ForeignKey, select
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncSession

from .main import Base

class Game(Base):
    __tablename__ = 'bot_games'
    id: Mapped[int] = mapped_column('id', Integer, primary_key=True, autoincrement=True, nullable=False)
    name: Mapped[str] = mapped_column('name', String(100), unique=True, nullable=False)

    @classmethod
    async def get_game_by_name(cls, session: AsyncSession, game_name:str):
        stmt = select(Game).where(Game.name == game_name)
        game = await session.scalar(stmt)

        return game
    
    @classmethod
    async def get_all_games(cls, session: AsyncSession):
        stmt = select(Game)
        games_stream = await session.stream_scalars(stmt)

        async for game in games_stream:
            yield game
    
    @classmethod
    async def add_game(cls, session: AsyncSession, game_name:str):
        new_game = cls(name=game_name)
        session.add(new_game)
        await session.flush()

        return new_game

class Score(Base):
    __tablename__ = 'bot_scores'
    id: Mapped[int] = mapped_column('id', Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id: Mapped[int] = mapped_column('user_id', ForeignKey('bot_users.id'))
    game_id: Mapped[int] = mapped_column('game_id', ForeignKey('bot_games.id'))
    amount_won: Mapped[int] = mapped_column('amount_won', Integer, nullable=False)
    timestamp: Mapped[datetime] = mapped_column('timestamp', DateTime, nullable=False, default=datetime.now())

    @classmethod
    async def add_score_by_game_name(cls, session: AsyncSession, uid:int, game_name:str, amount_won:int | None = None):
        game = await Game.get_game_by_name(session, game_name)

        if game is None:
            raise ValueError(f'No game found with name {game_name}')

        new_score = Score(user_id = uid, game_id = game.id, amount_won = amount_won)
        session.add(new_score)
        await session.flush()

        return new_score