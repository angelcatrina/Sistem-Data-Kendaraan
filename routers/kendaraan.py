from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.kendaraan import Kendaraan
from models.merk import Merk
from models.user import User
from schemas.kendaraan import KendaraanCreate, KendaraanUpdate, KendaraanResponse
from auth.security import get_current_user

router = APIRouter(prefix="/kendaraan", tags=["Kendaraan"])

@router.get("/", response_model=list[KendaraanResponse])
def get_all_kendaraan(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)  # <--- Gembok ditambahkan di sini
):
    return db.query(Kendaraan).all()

@router.get("/{kendaraan_id}", response_model=KendaraanResponse)
def get_kendaraan(
    kendaraan_id: int, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)  # <--- Gembok ditambahkan di sini
):
    kendaraan = db.query(Kendaraan).filter(Kendaraan.id == kendaraan_id).first()
    if not kendaraan:
        raise HTTPException(status_code=404, detail="Kendaraan tidak ditemukan")
    return kendaraan

@router.post("/", response_model=KendaraanResponse, status_code=201)
def create_kendaraan(
    data: KendaraanCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if not db.query(Merk).filter(Merk.id == data.merk_id).first():
        raise HTTPException(status_code=404, detail="Merk tidak ditemukan")
    if db.query(Kendaraan).filter(Kendaraan.nomor_plat == data.nomor_plat).first():
        raise HTTPException(status_code=400, detail="Nomor plat sudah terdaftar")
    
    kendaraan = Kendaraan(**data.model_dump(), user_id=current_user.id)
    db.add(kendaraan)
    db.commit()
    db.refresh(kendaraan)
    return kendaraan

@router.put("/{kendaraan_id}", response_model=KendaraanResponse)
def update_kendaraan(
    kendaraan_id: int,
    data: KendaraanUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    kendaraan = db.query(Kendaraan).filter(Kendaraan.id == kendaraan_id).first()
    if not kendaraan:
        raise HTTPException(status_code=404, detail="Kendaraan tidak ditemukan")
    if kendaraan.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Tidak punya izin mengubah data ini")
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(kendaraan, key, value)
    db.commit()
    db.refresh(kendaraan)
    return kendaraan

@router.delete("/{kendaraan_id}", status_code=204)
def delete_kendaraan(
    kendaraan_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    kendaraan = db.query(Kendaraan).filter(Kendaraan.id == kendaraan_id).first()
    if not kendaraan:
        raise HTTPException(status_code=404, detail="Kendaraan tidak ditemukan")
    if kendaraan.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Tidak punya izin menghapus data ini")
    db.delete(kendaraan)
    db.commit()