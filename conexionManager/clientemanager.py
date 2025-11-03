import psycopg
from models import Cliente


class ClienteManager:
    
    def addClient(self, cliente:Cliente, cursor:psycopg.Cursor):
        cursor.execute(
            "INSERT INTO cliente (nombre, telefono) VALUES (%s,%s)",
            (cliente.nombre, cliente.telefono)
        )
        return f"cliente creado"
    
    def getClientes(self, cursor: psycopg.Cursor) -> list:
        res = cursor.execute("SELECT id ,nombre FROM cliente").fetchall()
        return [{"id": row[0], "nombre": row[1]} for row in res]


    
    def getClienteForId(self, id: int, cursor: psycopg.Cursor) -> list:
        res = cursor.execute(
            "SELECT id,nombre FROM cliente WHERE id = %s", (id,)
        ).fetchall()
        return [{"id": row[0], "nombre": row[1]} for row in res]
     
    def ModificarClient(
        self, id: int, acutalizadoClient: Cliente, cursor: psycopg.Cursor
    ) -> str:
        cursor.execute(
            "UPDATE cliente SET nombre = %s WHERE id = %s",
            (acutalizadoClient.nombre, id),
        )
        return "Cliente modificado!"

    def deleteClient(self, id: int, cursor: psycopg.Cursor) -> str:
        cursor.execute("DELETE FROM cliente WHERE id = %s", (id,))
        return "Cliente eliminado"