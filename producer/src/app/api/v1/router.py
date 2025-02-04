from fastapi import APIRouter

from app.api.v1.routes.event import router as user_event

router = APIRouter(prefix="/api/v1")

router.include_router(
    user_event, prefix="/notifications", tags=["Пользовательские уведомления"]
)
