from fastapi import APIRouter

from .messages.routes import router as router_messages
from .usage.routes import router as router_usage

router = APIRouter(prefix='/ai')
router.include_router(router_messages)
router.include_router(router_usage)