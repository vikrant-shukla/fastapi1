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

    @classmethod
    def update_user(cls, id, **kw):
        obj = db.query(CrudSchema).filter(CrudSchema.id == id)
        for key, value in kw.items():
            obj.update({key: value})
        db.commit()

    @classmethod
    def delete_user(cls, id):
        obj = db.query(CrudSchema).filter(CrudSchema.id == id)
        obj.delete()
        db.commit()
