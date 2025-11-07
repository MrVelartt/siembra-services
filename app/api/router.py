from fastapi import APIRouter
from app.api.endpoints import proyectos, ofertas, demandas

api_router = APIRouter()
api_router.include_router(proyectos.router)
api_router.include_router(ofertas.router)
api_router.include_router(demandas.router)