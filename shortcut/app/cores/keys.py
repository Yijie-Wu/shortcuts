import json

from sqlalchemy.orm import Session

from app.models import Keys
from app.responses import ResponseException


def getAllKeys(db: Session):
    datas = db.query(Keys).all()

    return [
        {'id': k.id, 'id_': str(k.id_), 'type': k.type, 'name1': k.name1, 'name2': k.name2} for k in datas
    ]
