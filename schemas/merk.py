from pydantic import BaseModel
from datetime import datetime

class MerkCreate(BaseModel):
    nama: str
    negara_asal: str

class MerkUpdate(BaseModel):
    nama: str | None = None
    negara_asal: str | None = None

class MerkResponse(BaseModel):
    id: int
    nama: str
    negara_asal: str
    created_at: datetime

    model_config = {"from_attributes": True}