import psycopg
from conexionManager.productomanager import ProductosManager
from conexionManager.conexionmanagersupabase import getCursor
from fastapi import APIRouter, Depends
from models import Producto

ProdManager = ProductosManager()
router = APIRouter(prefix="/productos", tags=["Productos router"])


@router.get("/obtener_productos")
def getProductos(cursor: psycopg.Cursor = Depends(getCursor)):
    res = ProdManager.getProductos(cursor)
    return res


@router.post("/crear_productos")
def postProductos(producto: Producto, cursor: psycopg.Cursor = Depends(getCursor)):
    res = ProdManager.addProducto(producto, cursor)
    return {"msg": res}