from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, VARCHAR, INTEGER, TEXT

Base = declarative_base()
metadata = Base.metadata


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
