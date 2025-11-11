from fastapi import APIRouter, Depends, Query, Response
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.utils import normalize
from app.db.pagination import parse_range
from app.models.demandas import Demanda
from app.schemas.demandas import DemandaBase

router = APIRouter(prefix="/demandas", tags=["Demandas"])

@router.get("/", response_model=list[DemandaBase])
def listar_demandas(
    response: Response,
    range: str | None = Query(None, description="Formato: start-end, ej: 0-49"),
    departamento: str | None = None,
    especie: str | None = None,
    cadena: str | None = None,
    region: str | None = None,
    db: Session = Depends(get_db)
):
    offset, limit = parse_range(range)

    base_query = db.query(Demanda)

    if departamento:
        base_query = base_query.filter(normalize(Demanda.Dep_Desc).ilike(f"%{departamento}%"))
    if especie:
        base_query = base_query.filter(normalize(Demanda.Esp_Desc).ilike(f"%{especie}%"))
    if cadena:
        base_query = base_query.filter(normalize(Demanda.Cad_Desc).ilike(f"%{cadena}%"))
    if region:
        base_query = base_query.filter(normalize(Demanda.Reg_Desc).ilike(f"%{region}%"))

    total = base_query.count()
    data = base_query.order_by(Demanda.Dem_Titulo).offset(offset).limit(limit).all()

    end = offset + len(data) - 1 if data else offset
    response.headers["Content-Range"] = f"{offset}-{end}/{total}"
    response.headers["Accept-Ranges"] = "items"

    return data
