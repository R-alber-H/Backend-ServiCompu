from sqlalchemy.orm import Session, joinedload

from app.models.user import User

class UserRepository:
    
    def __init__(self,db: Session):
        self.db = db
        
    def get_by_email(self, email: str) -> User | None:
        return (
            self.db.query(User)
            .options(joinedload(User.role))
            .filter(User.email == email)
            .first()
        )
    
    def create(self, user: User) -> User:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def get_all(self):
        return (
            self.db.query(User)
            .options(joinedload(User.role))
            .all()
        )
        
    def get_by_id(self,id: int) ->  User | None:
        return(
            self.db.query(User)
            .options(joinedload(User.role))
            .filter(User.id == id)
            .first()  
        )
        
    def get_by_dni(self,dni:str) ->  User | None:
        return(
            self.db.query(User)
            .options(joinedload(User.role))
            .filter(User.dni == dni)
            .first()
        )
    
    def update(self, user: User,data:dict) -> User:
        for key, value in data.items():
           setattr(user,key,value)
        self.db.commit()
        self.db.refresh(user)
        return user
    
        
    
