import json

from sqlalchemy.orm import Session

from app.models import Mouse
from app.responses import ResponseException


def getAllMouse(db: Session):
    datas = db.query(Mouse).all()

    return [
        {'id': k.id, 'id_': str(k.id_), 'name': k.name} for k in datas
    ]
