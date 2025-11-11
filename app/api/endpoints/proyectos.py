from fastapi import APIRouter, Depends, Query, Response
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.utils import normalize
from app.db.pagination import parse_range
from app.models.proyectos import Proyecto
from app.schemas.proyectos import ProyectoBase

router = APIRouter(prefix="/proyectos", tags=["Proyectos"])


@router.get("/", response_model=list[ProyectoBase])
def listar_proyectos(
    response: Response,
    range: str | None = Query(None, description="Formato: start-end, ej: 0-49"),
    departamento: str | None = None,
    especie: str | None = None,
    cadena: str | None = None,
    db: Session = Depends(get_db)
):
    offset, limit = parse_range(range)

    base_query = db.query(Proyecto)

    if departamento:
        base_query = base_query.filter(normalize(Proyecto.Dep_Desc).ilike(f"%{departamento}%"))
    if especie:
        base_query = base_query.filter(normalize(Proyecto.Esp_Desc).ilike(f"%{especie}%"))
    if cadena:
        base_query = base_query.filter(normalize(Proyecto.Cad_Desc).ilike(f"%{cadena}%"))

    total = base_query.count()

    data = (
        base_query
        .order_by(Proyecto.Proy_Titulo)
        .offset(offset)
        .limit(limit)
        .all()
    )

    end = offset + len(data) - 1 if data else offset
    response.headers["Content-Range"] = f"{offset}-{end}/{total}"
    response.headers["Accept-Ranges"] = "items"

    return data
