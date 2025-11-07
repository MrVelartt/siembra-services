from sqlalchemy import Column, String, Integer, Text
from app.db.session import Base

class Demanda(Base):
    __tablename__ = "Demandas"

    Id = Column(String, primary_key=True, index=True)

    Dem_Id = Column(Integer, nullable=True)
    Dem_Titulo = Column(String, nullable=True)
    Dem_Desc = Column(Text, nullable=True)

    Esp_Id = Column(String, nullable=True)
    Esp_Desc = Column(String, nullable=True)

    Dep_Id = Column(String, nullable=True)
    Dep_Desc = Column(String, nullable=True)

    Reg_Id = Column(String, nullable=True)
    Reg_Desc = Column(String, nullable=True)

    Cad_Id = Column(String, nullable=True)
    Cad_Desc = Column(String, nullable=True)
