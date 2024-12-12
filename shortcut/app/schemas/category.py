from typing import Optional

from pydantic import BaseModel


class CategoryBase(BaseModel):
    type: str
    name: str
    desc: str


class CreateCategory(CategoryBase):
    pass


class UpdateCategory(CategoryBase):
    pass
