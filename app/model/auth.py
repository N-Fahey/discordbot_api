from datetime import datetime
from sqlalchemy import String, Boolean, DateTime, CHAR
from sqlalchemy.orm import Mapped, mapped_column

from .main import Base

class KeyAuth(Base):
    __tablename__ = 'bot_auth'
    api_key: Mapped[str] = mapped_column('api_key', CHAR(32), primary_key=True)
    name: Mapped[str] = mapped_column('name', String(32), unique=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column('created_at', DateTime, nullable=False, default=datetime.now)
    active: Mapped[bool] = mapped_column('active', Boolean, nullable=False)
