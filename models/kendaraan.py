from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class Kendaraan(Base):
    __tablename__ = "kendaraan"

    id = Column(Integer, primary_key=True, index=True)
    merk_id = Column(Integer, ForeignKey("merk.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    model = Column(String, nullable=False)
    tahun = Column(Integer, nullable=False)
    warna = Column(String, nullable=False)
    nomor_plat = Column(String, unique=True, nullable=False)
    harga = Column(Float, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relasi balik
    merk = relationship("Merk", back_populates="kendaraan")
    pemilik = relationship("User", back_populates="kendaraan")