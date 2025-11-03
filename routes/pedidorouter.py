import psycopg
from conexionManager.pedidomanager import PedidoManager
from conexionManager.conexionmanagersupabase import getCursor
from fastapi import APIRouter, Depends
from models import Pedido


PedidoManager = PedidoManager()
router = APIRouter(prefix="/pedidos", tags=["Pedidos router"])



@router.get("/obtener_pedidos")
def getobtenerPedido(cursor: psycopg.Cursor = Depends(getCursor)):
    res = PedidoManager.getobtenerPedido(cursor)
    return res


@router.get("/obtener_pedido/{id}")
def getPedidoporId(id: int, cursor: psycopg.Cursor = Depends(getCursor)):
    res = PedidoManager.getPedidoporId(id, cursor)
    return res


@router.get("/obtener_pedido_por_cliente/{nombre}")
def getPedidoporCliente(nombre: str, cursor: psycopg.Cursor = Depends(getCursor)):
    res = PedidoManager.getPedidoporCliente(nombre, cursor)
    return res