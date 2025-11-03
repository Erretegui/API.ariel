from pydantic import BaseModel

class Pedido(BaseModel):
    id_producto: int
    id_cliente: int
    cantidad: int


class Cliente(BaseModel):
    nombre: str
    telefono: int

class Producto(BaseModel):
    nombre: str
    precio: int
    
