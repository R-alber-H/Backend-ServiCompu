
from typing import TypeVar, Generic, Type
from sqlalchemy.orm import Session

T = TypeVar("T")

class BaseRepository(Generic[T]):
    def __init__(self, db: Session, model: Type[T]):
        self.db = db
        self.model = model

    def get_all(self) -> list[T]:
        return self.db.query(self.model).all()

    def get_by_name(self, name: str) -> T | None:
        return self.db.query(self.model).filter(self.model.name == name).first()

    def create(self, obj: T) -> T:
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj