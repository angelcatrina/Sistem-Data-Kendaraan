# Sistem Manajemen Data Kendaraan (RESTful API)

## 📝 Deskripsi Proyek
Sistem Data Kendaraan adalah aplikasi backend berbasis **RESTful API** yang dikembangkan menggunakan framework **FastAPI**. Sistem ini dirancang untuk mengelola data kendaraan secara terstruktur dengan relasi antar entitas (User, Merk, dan Kendaraan). Untuk menjamin keamanan data, sistem ini dilengkapi dengan fitur autentikasi berbasis **JWT (JSON Web Token)**.

### 🏗️ Arsitektur Domain
Proyek ini memiliki tiga domain utama:
1.  **User**: Pengguna terdaftar yang dapat memiliki kendaraan.
2.  **Merk**: Katalog merk kendaraan (Master Data).
3.  **Kendaraan**: Unit kendaraan yang terhubung ke satu pemilik (User) dan satu brand (Merk).

---

## 🛠️ Tech Stack
* **Framework:** FastAPI 0.135
* **Server:** Uvicorn (ASGI Server)
* **ORM:** SQLAlchemy 2.0
* **Database:** SQLite
* **Autentikasi:** JWT Bearer Token (OAuth2 Password Flow)
* **Keamanan:** `python-jose` (JWT) & `bcrypt` (Password Hashing)
* **Validasi:** Pydantic Schemas

---

## 📊 Struktur Folder
Proyek menggunakan pendekatan **Modular Structure** untuk memastikan kode tetap bersih dan mudah dipelihara:

```plaintext
sistem_kendaraan/
├── main.py              # Entry point aplikasi
├── database.py          # Konfigurasi database & session
├── models/              # Definisi tabel database (SQLAlchemy)
│   ├── user.py
│   ├── merk.py
│   └── kendaraan.py
├── schemas/             # Validasi data & response (Pydantic)
│   ├── user.py
│   ├── merk.py
│   └── kendaraan.py
├── routers/             # Implementasi endpoint API
│   ├── auth.py
│   ├── merk.py
│   └── kendaraan.py
└── auth/                # Logika keamanan & JWT
    └── security.py
```

---

## 🛰️ Daftar Endpoint Utama

### 🔐 Autentikasi (`/auth`)
| Method | Endpoint | Deskripsi |
| :--- | :--- | :--- |
| `POST` | `/auth/register` | Registrasi akun pengguna baru |
| `POST` | `/auth/login` | Login & mendapatkan JWT Access Token |

### 🏭 Merk Kendaraan (`/merk`)
*Semua endpoint di bawah memerlukan Header `Authorization: Bearer <token>`*

| Method | Endpoint | Deskripsi |
| :--- | :--- | :--- |
| `GET` | `/merk/` | Mengambil semua data merk |
| `POST` | `/merk/` | Menambah merk baru |
| `PUT` | `/merk/{id}` | Update data merk berdasarkan ID |
| `DELETE` | `/merk/{id}` | Hapus merk berdasarkan ID |

### 🚘 Kendaraan (`/kendaraan`)
| Method | Endpoint | Deskripsi |
| :--- | :--- | :--- |
| `GET` | `/kendaraan/` | Mengambil semua data kendaraan pengguna |
| `POST` | `/kendaraan/` | Tambah unit baru (Otomatis terikat ke User login) |
| `PUT` | `/kendaraan/{id}` | Update (Hanya berlaku untuk pemilik data) |
| `DELETE` | `/kendaraan/{id}` | Hapus (Hanya berlaku untuk pemilik data) |

---

## 🚀 Cara Menjalankan Proyek

1.  **Clone Repositori**
    ```bash
   git clone https://github.com/angelcatrina/Sistem-Data-Kendaraan.git
cd Sistem-Data-Kendaraan
    ```

2.  **Install Dependensi**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Jalankan Server**
    ```bash
    uvicorn main:app --reload
    ```

4.  **Akses Dokumentasi Interaktif**
    Buka [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) di browser Anda untuk mencoba API langsung melalui **Swagger UI**.

---
