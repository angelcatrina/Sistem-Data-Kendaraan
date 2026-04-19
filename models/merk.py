from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class Merk(Base):
    __tablename__ = "merk"

    id = Column(Integer, primary_key=True, index=True)
    nama = Column(String, unique=True, index=True, nullable=False)
    negara_asal = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relasi One-to-Many ke kendaraan
    kendaraan = relationship("Kendaraan", back_populates="merk")