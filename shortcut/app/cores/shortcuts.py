import json

from sqlalchemy import and_
from sqlalchemy.orm import Session

from app.models import Shortcut
from app.responses import ResponseException
from app.schemas.shortcuts import CreateShortcut, UpdateShortcut


def getAllSystemShortcuts(db: Session):
    datas = db.query(Shortcut).all()

    return [
        {
            'id': d.id,
            'tag': d.tag,
            'type': d.type,
            'content': json.loads(d.content),
            'conflict': json.loads(d.conflict),
            'function': d.function,
            'function_en': d.function_en,
            'category_name': d.category.name
        } for d in datas if d.category.type == 'Windows'
    ]


def getAllVscodeShortcuts(db: Session):
    datas = db.query(Shortcut).all()

    return [
        {
            'id': d.id,
            'tag': d.tag,
            'type': d.type,
            'content': json.loads(d.content),
            'conflict': json.loads(d.conflict),
            'function': d.function,
            'function_en': d.function_en,
            'category_name': d.category.name
        } for d in datas if d.category.type == 'Vscode'
    ]


def getAllAccotestShortcuts(db: Session):
    datas = db.query(Shortcut).all()

    return [
        {
            'id': d.id,
            'tag': d.tag,
            'type': d.type,
            'content': json.loads(d.content),
            'conflict': json.loads(d.conflict),
            'function': d.function,
            'function_en': d.function_en,
            'category_name': d.category.name
        } for d in datas if d.category.type == 'Accotest'
    ]


def createAccotestShortcuts(shortcut: CreateShortcut, db: Session):
    new_item = Shortcut(
        tag=shortcut.tag,
        type=shortcut.type,
        function=shortcut.function,
        function_en=shortcut.function_en,
        category_id=shortcut.category_id,
        content=json.dumps({"content": shortcut.content})
    )

    db.add(new_item)
    db.commit()
    db.refresh(new_item)

    # 开始计算冲突

    return {
        'id': new_item.id,
        'tag': new_item.tag,
        'type': new_item.type,
        'function': new_item.function,
        'function_en': new_item.function_en,
        'category_id': new_item.category_id,
        'category_name': new_item.category.name,
        'content': json.loads(new_item.content)
    }


def createSystemShortcuts(shortcut: CreateShortcut, db: Session):
    new_item = Shortcut(
        tag=shortcut.tag,
        type=shortcut.type,
        function=shortcut.function,
        function_en=shortcut.function_en,
        category_id=shortcut.category_id,
        content=json.dumps({"content": shortcut.content})
    )

    db.add(new_item)
    db.commit()
    db.refresh(new_item)

    return {
        'id': new_item.id,
        'tag': new_item.tag,
        'type': new_item.type,
        'function': new_item.function,
        'function_en': new_item.function_en,
        'category_id': new_item.category_id,
        'category_name': new_item.category.name,
        'content': json.loads(new_item.content)
    }


def createVscodeShortcuts(shortcut: CreateShortcut, db: Session):
    new_item = Shortcut(
        tag=shortcut.tag,
        type=shortcut.type,
        function=shortcut.function,
        function_en=shortcut.function_en,
        category_id=shortcut.category_id,
        content=json.dumps({"content": shortcut.content})
    )

    db.add(new_item)
    db.commit()
    db.refresh(new_item)

    return {
        'id': new_item.id,
        'tag': new_item.tag,
        'type': new_item.type,
        'function': new_item.function,
        'function_en': new_item.function_en,
        'category_id': new_item.category_id,
        'category_name': new_item.category.name,
        'content': json.loads(new_item.content)
    }
