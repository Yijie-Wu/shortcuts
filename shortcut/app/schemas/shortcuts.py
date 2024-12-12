from typing import Optional

from pydantic import BaseModel


class ShortcutBase(BaseModel):
    tag: str
    type: str
    function: str
    content: list
    function_en: str
    category_id: int


class CreateShortcut(ShortcutBase):
    pass


class UpdateShortcut(ShortcutBase):
    pass
