
from app.models.suppliers import Supplier
from app.repositories.supplier_repository import SupplierRepository
from app.schemas.supplier import SupplierCreate

class SupplierService():
    def __init__(self, repo:SupplierRepository):
        self.repo = repo
    
    def create_supplier(self,supplier:SupplierCreate):
        supplier_exists = self.repo.get_by_name(supplier.name)
        if supplier_exists:
            raise ValueError(f"El proveedor con nombre {supplier.name} ya esta registrado")
        new_supplier = Supplier(
            name = supplier.name,
            phone = supplier.phone or "Sin telefono"
        )
        return self.repo.create(new_supplier)
    
    def get_all(self):
        return self.repo.get_all()