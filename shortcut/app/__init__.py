import json
import os.path

from fastapi import FastAPI

from app.apis import router
from app.utils.mouse import MOUSE
from app.utils.keyboard import KEYS
from app.middlewares import add_cors_middleware
from app.models import Keys, Mouse, Category, Shortcut
from app.extensions import generate_tables, SessionLocal
from app.settings import Settings, load_app_settings, BASE_DIR


def create_app() -> FastAPI:
    settings = load_app_settings()

    app = FastAPI(
        title=settings.APP_TITLE,
        version=settings.APP_VERSION,
        description=settings.APP_DESCRIPTION
    )

    register_router(app, settings)
    init_dirs(settings)
    register_middlewares(app, settings)
    register_databases()

    return app


def register_router(app: FastAPI, settings: Settings):
    app.include_router(router, prefix=settings.GLOBAL_API_PREFIX)


def register_middlewares(app: FastAPI, settings: Settings):
    add_cors_middleware(app, settings)


def register_databases():
    generate_tables()
    init_mouse()
    init_keys()
    init_category()
    init_system_shortcuts()
    init_vscode_shortcuts()


def init_dirs(settings: Settings):
    if not os.path.exists(BASE_DIR):
        os.makedirs(BASE_DIR, exist_ok=True)

    if not os.path.exists(settings.ASSETS_DIR):
        os.makedirs(settings.ASSETS_DIR, exist_ok=True)


def init_mouse():
    db = SessionLocal()
    for item in MOUSE:
        check = db.query(Mouse).filter(Mouse.id_ == item.get('id')).first()
        if not check:
            new_item = Mouse(
                id_=item.get('id'),
                name=item.get('name')
            )
            db.add(new_item)
            db.commit()
            db.refresh(new_item)
        else:
            check.name = item.get('name')
            db.commit()

    db.close()


def init_keys():
    db = SessionLocal()
    for item in KEYS:
        check = db.query(Keys).filter(Keys.id_ == item.get('id')).first()
        if not check:
            new_item = Keys(
                id_=item.get('id'),
                type=item.get('type'),
                name1=item.get('name1'),
                name2=item.get('name2')
            )
            db.add(new_item)
            db.commit()
            db.refresh(new_item)
        else:
            check.type = item.get('type')
            check.name1 = item.get('name1')
            check.name2 = item.get('name2')
            db.commit()

    db.close()


def init_category():
    db = SessionLocal()
    for name, desc in [
        ('System', 'Windows操作系统快捷键'),
        ('VsCode', 'VsCode自带快捷键')
    ]:
        category_check = db.query(Category).filter(Category.name == name).first()
        if not category_check:
            new_category = Category(name=name, desc=desc)
            db.add(new_category)
            db.commit()
            db.refresh(new_category)
        else:
            category_check.desc = desc
            db.commit()

    db.close()


def init_vscode_shortcuts():
    pass


def init_system_shortcuts():
    pass
