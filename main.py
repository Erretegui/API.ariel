from fastapi import FastAPI
from routes.clienterouter import router as routerCliente
from routes.pedidorouter import router as routerPedidos
from routes.productosrouter import router as routerProductos  


app = FastAPI()


app.include_router(routerCliente)
app.include_router(routerPedidos)
app.include_router(routerProductos)


