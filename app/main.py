from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse

from app.routes.main import router as api_router
from .auth import check_api_key

app = FastAPI(title='Discordbot-API')

app.include_router(api_router, dependencies=[Depends(check_api_key)])

@app.get('/', include_in_schema=False)
async def root() -> JSONResponse:
    return JSONResponse({
        'message': "Hello World"
    })

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='localhost', port=8000)