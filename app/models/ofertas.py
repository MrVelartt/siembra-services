from sqlalchemy import Column, String, Integer, Text
from app.db.session import Base

class Oferta(Base):
    __tablename__ = "Ofertas"

    Id = Column(String, primary_key=True, index=True)  # UUID -> str en Python

    Ofer_Id = Column(Integer, nullable=True)  # <- 🔥 Antes String, ahora correcto
    Ofer_Titulo = Column(String, nullable=True)
    Ofer_Desc = Column(Text, nullable=True)  # <- Text para descripciones largas

    Esp_Id = Column(String, nullable=True)
    Esp_Desc = Column(String, nullable=True)

    Cad_Id = Column(String, nullable=True)
    Cad_Desc = Column(String, nullable=True)

    Ciu_Id = Column(String, nullable=True)
    Ciu_Desc = Column(String, nullable=True)

    Dep_Id = Column(String, nullable=True)
    Dep_Desc = Column(String, nullable=True)

    Reg_Id = Column(String, nullable=True)
    Reg_Desc = Column(String, nullable=True)

    Pais_Id = Column(String, nullable=True)
    Pais_Desc = Column(String, nullable=True)
