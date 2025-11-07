from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.db.session import get_db
from app.models.demandas import Demanda
from app.schemas.demandas import DemandaBase

router = APIRouter(prefix="/demandas", tags=["Demandas"])

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

@router.get("/", response_model=list[DemandaBase])
def listar_demandas(
    departamento: str | None = None,
    especie: str | None = None,
    cadena: str | None = None,
    region: str | None = None,
    limit: int = 50,
    offset: int = 0,
    db: Session = Depends(get_db)
):
    query = db.query(Demanda)

    if departamento:
        query = query.filter(normalize(Demanda.Dep_Desc).like(f"%{departamento.lower()}%"))

    if especie:
        query = query.filter(normalize(Demanda.Esp_Desc).like(f"%{especie.lower()}%"))

    if cadena:
        query = query.filter(normalize(Demanda.Cad_Desc).like(f"%{cadena.lower()}%"))

    if region:
        query = query.filter(normalize(Demanda.Reg_Desc).like(f"%{region.lower()}%"))

    return query.order_by(Demanda.Dem_Titulo).offset(offset).limit(limit).all()
