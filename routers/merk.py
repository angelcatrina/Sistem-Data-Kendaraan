from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.merk import Merk
from models.user import User
from schemas.merk import MerkCreate, MerkUpdate, MerkResponse
from auth.security import get_current_user

router = APIRouter(prefix="/merk", tags=["Merk Kendaraan"])

@router.get("/", response_model=list[MerkResponse])
def get_all_merk(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)  # Gembok ditambahkan di sini
):
    return db.query(Merk).all()

@router.get("/{merk_id}", response_model=MerkResponse)
def get_merk(
    merk_id: int, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)  # Gembok ditambahkan di sini
):
    merk = db.query(Merk).filter(Merk.id == merk_id).first()
    if not merk:
        raise HTTPException(status_code=404, detail="Merk tidak ditemukan")
    return merk

@router.post("/", response_model=MerkResponse, status_code=201)
def create_merk(
    merk_data: MerkCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)  # Endpoint terproteksi JWT
):
    if db.query(Merk).filter(Merk.nama == merk_data.nama).first():
        raise HTTPException(status_code=400, detail="Merk sudah ada")
    merk = Merk(**merk_data.model_dump())
    db.add(merk)
    db.commit()
    db.refresh(merk)
    return merk

@router.put("/{merk_id}", response_model=MerkResponse)
def update_merk(
    merk_id: int,
    merk_data: MerkUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    merk = db.query(Merk).filter(Merk.id == merk_id).first()
    if not merk:
        raise HTTPException(status_code=404, detail="Merk tidak ditemukan")
    for key, value in merk_data.model_dump(exclude_unset=True).items():
        setattr(merk, key, value)
    db.commit()
    db.refresh(merk)
    return merk

@router.delete("/{merk_id}", status_code=204)
def delete_merk(
    merk_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    merk = db.query(Merk).filter(Merk.id == merk_id).first()
    if not merk:
        raise HTTPException(status_code=404, detail="Merk tidak ditemukan")
    db.delete(merk)
    db.commit()