import json

from sqlalchemy import and_
from sqlalchemy.orm import Session

from app.models import Category
from app.schemas.category import CreateCategory, UpdateCategory
from app.responses import ResponseException


def getAllCategories(db: Session):
    data = db.query(Category).all()

    return data


def createCategory(category: CreateCategory, db: Session):
    check = db.query(Category).filter(and_(
        Category.name == category.name.lower().strip(),
        Category.type == category.type.lower().strip()
    )).first()

    if check:
        return ResponseException.HTTP_409_CONFLICT

    new_item = Category(name=category.name.strip(), desc=category.desc, type=category.type)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)

    return new_item


def updateCategory(id: int, category: UpdateCategory, db: Session):
    item = db.query(Category).filter_by(id=id).first()
    if not item:
        return ResponseException.HTTP_404_NOT_FOUND

    item.name = category.name.strip()
    item.desc = category.desc.strip()
    item.type = category.type.strip()
    db.commit()
    db.refresh(item)

    return {'id': item.id, 'name': item.name, 'desc': item.desc, 'type': item.type}


def deleteCategory(id: int, db: Session):
    item = db.query(Category).filter_by(id=id).first()
    if not item:
        return ResponseException.HTTP_404_NOT_FOUND

    db.delete(item)
    db.commit()

    return {'detail': 'delete success'}
