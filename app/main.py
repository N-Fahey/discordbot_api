from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.routes.main import router as api_router

app = FastAPI(title='Discordbot-API')

app.include_router(api_router)

@app.get('/', include_in_schema=False)
async def root() -> JSONResponse:
    return JSONResponse({
        'message': "Hello World"
    })

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='localhost', port=8000)