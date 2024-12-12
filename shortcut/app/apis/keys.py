from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Query

from app.extensions import get_rdbms
from app.settings import load_app_settings
from app.cores.keys import getAllKeys

router = APIRouter()
settings = load_app_settings()


@router.get('/all', status_code=200, description='获取所有keys')
def keys(db: Session = Depends(get_rdbms)):
    return getAllKeys(db)

