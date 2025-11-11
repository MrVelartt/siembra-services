from fastapi import APIRouter, Depends, Query, Response
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.utils import normalize
from app.db.pagination import parse_range
from app.models.ofertas import Oferta
from app.schemas.ofertas import OfertaBase

router = APIRouter(prefix="/ofertas", tags=["Ofertas"])


@router.get("/", response_model=list[OfertaBase])
def listar_ofertas(
    response: Response,
    range: str | None = Query(None, description="Formato: start-end, ej: 0-49"),
    departamento: str | None = None,
    especie: str | None = None,
    cadena: str | None = None,
    region: str | None = None,
    ciudad: str | None = None,
    db: Session = Depends(get_db)
):
    offset, limit = parse_range(range)

    base_query = db.query(Oferta)

    if departamento:
        base_query = base_query.filter(normalize(Oferta.Dep_Desc).ilike(f"%{departamento}%"))
    if especie:
        base_query = base_query.filter(normalize(Oferta.Esp_Desc).ilike(f"%{especie}%"))
    if cadena:
        base_query = base_query.filter(normalize(Oferta.Cad_Desc).ilike(f"%{cadena}%"))
    if region:
        base_query = base_query.filter(normalize(Oferta.Reg_Desc).ilike(f"%{region}%"))
    if ciudad:
        base_query = base_query.filter(normalize(Oferta.Ciu_Desc).ilike(f"%{ciudad}%"))

    total = base_query.count()
    data = (
        base_query
        .order_by(Oferta.Ofer_Titulo)
        .offset(offset)
        .limit(limit)
        .all()
    )

    end = offset + len(data) - 1 if data else offset
    response.headers["Content-Range"] = f"{offset}-{end}/{total}"
    response.headers["Accept-Ranges"] = "items"

    return data
