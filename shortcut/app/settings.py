import os
import sys
from typing import List

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
STATIC_DIR = os.path.join(BASE_DIR, 'app', 'static')


class Settings:
    APP_TITLE: str = 'Shortcuts'
    APP_VERSION: str = '1.0.0'
    APP_DESCRIPTION: str = '[Shortcuts] 快捷键生成系统.'

    GLOBAL_API_PREFIX: str = ''
    DATAS_DIR: str = os.path.join(BASE_DIR, 'datas')
    ASSETS_DIR: str = os.path.join(DATAS_DIR, 'assets')

    AUTO_FLASH: bool = True
    PREFIX: str = 'sqlite:///' if sys.platform.startswith('win') else 'sqlite:////'
    DATABASE_URL: str = PREFIX + os.path.join(DATAS_DIR, 'data.db')

    ALLOW_METHODS: List[str] = ["*"]
    ALLOW_HEADERS: List[str] = ["*"]
    ALLOW_ORIGINS: List[str] = ["*", ""]
    ALLOW_CREDENTIALS: bool = True


def load_app_settings() -> Settings:
    settings = Settings()
    return settings
