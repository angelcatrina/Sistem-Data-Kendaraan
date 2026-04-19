from fastapi import FastAPI
from database import engine, Base
from models import user, merk, kendaraan  # import semua models agar tabel terbuat
from routers import auth, merk as merk_router, kendaraan as kendaraan_router

# Buat semua tabel otomatis
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Sistem Data Kendaraan",
    description="RESTful API untuk mengelola data kendaraan berdasarkan merk",
    version="1.0.0"
)

# Daftarkan semua router
app.include_router(auth.router)
app.include_router(merk_router.router)
app.include_router(kendaraan_router.router)

@app.get("/", tags=["Root"])
def root():
    return {"message": "Selamat datang di Sistem Data Kendaraan API"}