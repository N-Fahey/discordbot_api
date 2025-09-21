from fastapi import Security, HTTPException
from fastapi.security import APIKeyHeader
from sqlalchemy import select

from .db import DBSessionDep
from app.model import KeyAuth

header_scheme = APIKeyHeader(name='X-API-KEY')

async def check_api_key(session: DBSessionDep, key: str = Security(header_scheme)):

    async with session.begin() as session:
        stmt = select(KeyAuth).where(KeyAuth.api_key == key).where(KeyAuth.active == True)
        matched_key = await session.scalar(stmt)
    
    if not matched_key:
        raise HTTPException(status_code=401, detail="Missing or invalid API key.")
