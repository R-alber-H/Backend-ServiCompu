from app.models.user import User
from app.repositories.role_repository import RoleRepository
from app.repositories.user_repositorry import UserRepository
from app.schemas.user import CustomerCreate, UserCreate


class UserService():
    def __init__(self,repo_user: UserRepository,repo_role :RoleRepository):
        self.repo = repo_user
        self.repo_role = repo_role
        
    def create_staff(self,user:UserCreate):
        user_exists = self.repo.get_by_email(user.email)
        if user_exists:
            raise ValueError("El usuario ya esta registrado")
        new_user = User(
            name = user.name,
            email = user.email,
            role_id = user.role_id
        )
        return self.repo.create(new_user)
    
    def create_customer(self,user:CustomerCreate):
        user_exits = self.repo.get_by_dni(user.dni)
        if user_exits:
            raise ValueError("El usuario ya esta registrado")
        role = self.repo_role.get_by_name("cliente")
        new_user = User(
            name = user.name,
            dni = user.dni,
            phone = user.phone,
            email = user.email,
            role_id = role.id
        )
        return self.repo.create(new_user)
    
    def get_all(self):
        return self.repo.get_all()