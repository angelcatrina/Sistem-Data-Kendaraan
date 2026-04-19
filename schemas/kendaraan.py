from pydantic import BaseModel, Field
from datetime import datetime

class KendaraanCreate(BaseModel):
    merk_id: int
    model: str
    tahun: int = Field(..., ge=1900, le=2100)
    warna: str
    nomor_plat: str
    harga: float = Field(..., gt=0)

class KendaraanUpdate(BaseModel):
    model: str | None = None
    tahun: int | None = Field(default=None, ge=1900, le=2100)
    warna: str | None = None
    nomor_plat: str | None = None
    harga: float | None = Field(default=None, gt=0)

class KendaraanResponse(BaseModel):
    id: int
    merk_id: int
    user_id: int
    model: str
    tahun: int
    warna: str
    nomor_plat: str
    harga: float
    created_at: datetime

    model_config = {"from_attributes": True}