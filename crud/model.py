from crud.schema import CrudSchema
from db.session import get_db

db = get_db()


class RegistrationModel:
    @classmethod
    def create(cls, **kw):
        obj = CrudSchema(**kw)
        try:
            db.add(obj)
            db.commit()
            db.refresh(obj)
            return obj
        except Exception as e:
            db.rollback()
            db.close()
            raise e

    @classmethod
    def get_user(cls, payload):
        obj = db.query(CrudSchema).filter(CrudSchema.username == payload).first()
        return obj
