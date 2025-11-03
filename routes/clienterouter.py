import psycopg
from fastapi import APIRouter, Depends
from conexionManager.clientemanager import ClienteManager
from models import Cliente
from conexionManager.conexionmanagersupabase import getCursor 


router = APIRouter(prefix="/clientes", tags=["Clientes routes"])
clientManager = ClienteManager()

@router.get("/obtener_clientes")
def getClientes(cursor: psycopg.Cursor = Depends(getCursor)):
    res = clientManager.getClientes(cursor)
    return res


@router.get("/obtener_cliente/{id}")
def getClienteForId(id: int, cursor: psycopg.Cursor = Depends(getCursor)):
    res = clientManager.getClienteForId(id, cursor)
    return res


@router.post("/crear_cliente")
def postCliente(cliente: Cliente, cursor: psycopg.Cursor = Depends(getCursor)):
    res = clientManager.addClient(cliente, cursor)
    return {"msg": res}


@router.put("/modificar_cliente/{id}")
def putCliente(
    id: int, clienteactualizado: Cliente, cursor: psycopg.Cursor = Depends(getCursor)
):
    res = clientManager.ModificarClient(id, clienteactualizado, cursor)
    return {"msg", res}


@router.delete("/eliminar_cliente/{id}")
def deleteCliente(id: int, cursor: psycopg.Cursor = Depends(getCursor)):
    res = clientManager.deleteClient(id, cursor)
    return {"msg": res}