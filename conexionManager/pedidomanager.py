import psycopg
from models import Pedido

class PedidoManager:


    def getobtenerPedido(self, cursor: psycopg.Cursor) -> list:
        res = cursor.execute(
            "SELECT producto.nombre, producto.precio, cliente.nombre FROM pedido INNER JOIN cliente ON pedido.id_cliente = cliente.id INNER JOIN producto ON pedido.id_pedido = producto.id_producto"
        ).fetchall()
        return [
            {"producto": row[0], "precio": row[1], "cliente": row[2]} for row in res
        ]

    def getPedidoporId(self, id: int, cursor: psycopg.Cursor) -> list:
        res = cursor.execute(
            "SELECT producto.nombre, producto.precio, cliente.nombre FROM pedido INNER JOIN cliente ON pedido.id_cliente = cliente.id INNER JOIN producto ON pedido.id_pedido=producto.id_producto WHERE pedido.id_cliente = %s",
            (id,),
        ).fetchall()
        return [
            {"producto": row[0], "precio": row[1], "cliente": row[2]} for row in res
        ]

    def getPedidoporCliente(self, nombre: str, cursor: psycopg.Cursor) -> list | str:
        idCliente = cursor.execute(
            "SELECT id FROM cliente WHERE nombre = (%s)", (nombre,)
        ).fetchone()
        print(idCliente)
        if idCliente:
            res = cursor.execute(
                "SELECT producto.nombre, producto.precio, cliente.nombre FROM pedido INNER JOIN cliente ON pedido.id_cliente = cliente.id INNER JOIN producto ON pedido.id_pedido = producto.id_producto WHERE pedido.id_cliente = %s",
                (idCliente[0],),
            ).fetchall() 
            return [
                {"producto": row[0], "precio": row[1], "cliente": row[2]} for row in res
            ]
        else:
            return "Error, usuario no encontrado"

    def addPedido(self, pedido: Pedido, cursor: psycopg.Cursor):
        cursor.execute(
            "INSERT INTO pedido (id_producto, id_cliente) VALUES (%s,%s)",
            (pedido.id_producto, pedido.id_cliente),
        )
        return "pedido agregado"