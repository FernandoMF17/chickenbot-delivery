from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

from app.api import admin

app = FastAPI(
    title="ChickenBot Delivery API",
    description="Backend para la gestión de pedidos",
    version="1.0.0"
)

app.add_middleware(
    SessionMiddleware,
    secret_key="super-secret-key"
)

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)

app.include_router(admin.router)

@app.get("/")
async def root():
    return {
        "mensaje": "Bienvenido a ChickenBot Delivery API",
        "estado": "Servidor funcionando correctamente"
    }