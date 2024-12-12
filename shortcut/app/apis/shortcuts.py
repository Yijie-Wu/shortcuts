from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Query

from app.extensions import get_rdbms
from app.settings import load_app_settings
from app.schemas.shortcuts import CreateShortcut, UpdateShortcut
from app.cores.shortcuts import getAllSystemShortcuts, getAllVscodeShortcuts, getAllAccotestShortcuts
from app.cores.shortcuts import createAccotestShortcuts, createSystemShortcuts, createVscodeShortcuts

router = APIRouter()
settings = load_app_settings()


@router.get('/system/all', status_code=200, description='获取所有系统快捷键')
def system_shortcuts(db: Session = Depends(get_rdbms)):
    return getAllSystemShortcuts(db)


@router.get('/vscode/all', status_code=200, description='获取所有Vscode快捷键')
def vscode_shortcuts(db: Session = Depends(get_rdbms)):
    return getAllVscodeShortcuts(db)


@router.get('/accotest/all', status_code=200, description='获取所有accotest快捷键')
def accotest_shortcuts(db: Session = Depends(get_rdbms)):
    return getAllAccotestShortcuts(db)


@router.post('/accotest/create', status_code=200, description='创建accotest快捷键')
def create_accotest_shortcut(shortcut: CreateShortcut, db: Session = Depends(get_rdbms)):
    return createAccotestShortcuts(shortcut, db)


@router.post('/system/create', status_code=200, description='创建system快捷键')
def create_accotest_shortcut(shortcut: CreateShortcut, db: Session = Depends(get_rdbms)):
    return createSystemShortcuts(shortcut, db)


@router.post('/vscode/create', status_code=200, description='创建vscode快捷键')
def create_accotest_shortcut(shortcut: CreateShortcut, db: Session = Depends(get_rdbms)):
    return createVscodeShortcuts(shortcut, db)
