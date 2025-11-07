from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.db.session import get_db
from app.models.ofertas import Oferta
from app.schemas.ofertas import OfertaBase

router = APIRouter(prefix="/ofertas", tags=["Ofertas"])

def normalize(col):
    return func.lower(
        func.replace(
            func.replace(
                func.replace(
                    func.replace(
                        func.replace(col, "á", "a"),
                    "é", "e"),
                "í", "i"),
            "ó", "o"),
        "ú", "u")
    )

@router.get("/", response_model=list[OfertaBase])
def listar_ofertas(
    departamento: str | None = None,
    especie: str | None = None,
    cadena: str | None = None,
    region: str | None = None,
    ciudad: str | None = None,
    limit: int = 50,
    offset: int = 0,
    db: Session = Depends(get_db)
):
    query = db.query(Oferta)

    if departamento:
        query = query.filter(normalize(Oferta.Dep_Desc).like(f"%{departamento.lower()}%"))

    if especie:
        query = query.filter(normalize(Oferta.Esp_Desc).like(f"%{especie.lower()}%"))

    if cadena:
        query = query.filter(normalize(Oferta.Cad_Desc).like(f"%{cadena.lower()}%"))

    if region:
        query = query.filter(normalize(Oferta.Reg_Desc).like(f"%{region.lower()}%"))

    if ciudad:
        query = query.filter(normalize(Oferta.Ciu_Desc).like(f"%{ciudad.lower()}%"))

    return query.order_by(Oferta.Ofer_Titulo).offset(offset).limit(limit).all()
