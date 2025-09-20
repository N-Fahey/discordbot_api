from fastapi import APIRouter

from .ai.routes import router as ai_router
from .bank.routes import router as bank_router
from .games.routes import router as games_router
from .scores.routes import router as scores_router
from .users.routes import router as users_router

router = APIRouter(prefix='/api/v1')
router.include_router(ai_router, tags=['AI'])
router.include_router(bank_router, tags=['Bank'])
router.include_router(games_router, tags=['Games'])
router.include_router(scores_router, tags=['Scores'])
router.include_router(users_router, tags=['Users'])