from fastapi import FastAPI

app = FastAPI(
    title="ChickenBot Delivery API",
    description="Backend para la gestión de pedidos de ChickenBot Delivery",
    version="1.0.0"
)


@app.get("/")
async def root():
    return {
        "mensaje": "Bienvenido a ChickenBot Delivery API",
        "estado": "Servidor funcionando correctamente"
    }