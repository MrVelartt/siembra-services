from pydantic import BaseModel

class OfertaBase(BaseModel):
    Id: str | None = None
    Ofer_Id: int | None = None
    Ofer_Titulo: str | None = None
    Ofer_Desc: str | None = None

    Esp_Id: str | None = None
    Esp_Desc: str | None = None

    Cad_Id: str | None = None
    Cad_Desc: str | None = None

    Ciu_Id: str | None = None
    Ciu_Desc: str | None = None

    Dep_Id: str | None = None
    Dep_Desc: str | None = None

    Reg_Id: str | None = None
    Reg_Desc: str | None = None

    Pais_Id: str | None = None
    Pais_Desc: str | None = None

    class Config:
        from_attributes = True
