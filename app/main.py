import logging

from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse

from app.routes.main import router as api_router
from app.auth import check_api_key
from app.log import HealthCheckFilter

app = FastAPI(title='Discordbot-API')

app.include_router(api_router, dependencies=[Depends(check_api_key)])

@app.get('/health', include_in_schema=False)
async def health_check() -> JSONResponse:
    return JSONResponse({
        'status': "healthy"
    })

logging.getLogger('uvicorn.access').addFilter(HealthCheckFilter())
