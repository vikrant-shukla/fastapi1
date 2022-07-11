from db.session import Base
from sqlalchemy import Column, VARCHAR, INTEGER, TEXT


class CrudSchema(Base):
    __tablename__ = "userTable"
    __table_args__ = {"schema": "application"}

    id = Column(INTEGER, primary_key=True)
    username = Column(TEXT)
    firstname = Column(VARCHAR(50), nullable=True)
    lastname = Column(VARCHAR(50), nullable=True)
    password = Column(TEXT)
    dob = Column(TEXT)
    mobileNumber = Column(INTEGER, default=1111111111)



