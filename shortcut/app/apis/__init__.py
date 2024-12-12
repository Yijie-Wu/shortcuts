from fastapi import APIRouter

from app.apis.keys import router as keys_router
from app.apis.mouse import router as mouse_router
from app.apis.category import router as category_router
from app.apis.shortcuts import router as shortcuts_router

router = APIRouter()

router.include_router(keys_router, prefix='/keys', tags=['键盘'])
router.include_router(mouse_router, prefix='/mouse', tags=['鼠标'])
router.include_router(category_router, prefix='/category', tags=['分类'])
router.include_router(shortcuts_router, prefix='/shortcut', tags=['快捷键'])
