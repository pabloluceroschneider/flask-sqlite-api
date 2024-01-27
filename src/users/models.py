from sqlalchemy import inspect
from datetime import datetime
from dataclasses import dataclass
from .. import db

@dataclass
class User(db.Model):
    id           = db.Column(db.String(50), primary_key=True, nullable=False, unique=True)
    created      = db.Column(db.DateTime(timezone=True), default=datetime.now)
    updated      = db.Column(db.DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)

    username     = db.Column(db.String(100), nullable=False)
    email        = db.Column(db.String(100), nullable=False, unique=True)
    phone_number = db.Column(db.String(20))

    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }
