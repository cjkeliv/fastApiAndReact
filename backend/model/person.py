from datetime import date
from sqlalchemy import Enum
from sqlmodel import SQLModel, Field, Relationship
from model.mixins import TimeMixin
from typing import Optional


class Sex(str, Enum):
    Male = "MALE"
    FEMALE = "FEMALE"

class Person(SQLModel,TimeMixin, table=True):
    ""
    __tablename__ = "person"
    id: Optional[str] = Field(None, primary_key=True, nullable=False)
    name: str
    birth: date
    sex: Sex
    profile: str
    phone_number: str
    users: Optional["users"] = Relationship(sa_relationship_kwargs={"uselist":False}, back_populates="person")
