from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Query

from app.extensions import get_rdbms
from app.settings import load_app_settings
from app.cores.category import getAllCategories, createCategory, updateCategory, deleteCategory
from app.schemas.category import CreateCategory, UpdateCategory

router = APIRouter()
settings = load_app_settings()


@router.get('/all', status_code=200, description='获取所有category')
def categories(db: Session = Depends(get_rdbms)):
    return getAllCategories(db)


@router.post('/create', status_code=200, description='创建category')
def create_category(category: CreateCategory, db: Session = Depends(get_rdbms)):
    return createCategory(category, db)


@router.put('/update/{id}', status_code=200, description='更新category')
def update_category(id: int, category: UpdateCategory, db: Session = Depends(get_rdbms)):
    return updateCategory(id, category, db)


@router.delete('/delete/{id}', status_code=200, description='删除category')
def delete_category(id: int, db: Session = Depends(get_rdbms)):
    return deleteCategory(id, db)
