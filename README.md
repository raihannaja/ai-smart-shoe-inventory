[![AI Smart Shoe CI-CD Pipeline](https://github.com/raihannaja/ai-smart-shoe-inventory/actions/workflows/cicd.yml/badge.svg)](https://github.com/raihannaja/ai-smart-shoe-inventory/actions/workflows/cicd.yml)

# 👟 AI Smart Shoe Inventory & Sales Automation System
> **Implementasi Autentik CI/CD & Otomatisasi Sistem Berbasis SDLC**

Perangkat lunak ini merupakan sistem asisten AI yang dirancang untuk membantu toko sepatu dalam mengotomatisasi pengelolaan stok, penjualan, rekomendasi produk, dan analisis tren pembelian pelanggan. 

Sistem ini terintegrasi dengan API Tukupatu (marketplace) dan sistem pembayaran digital untuk membantu proses transaksi secara otomatis. AI juga dapat memberikan rekomendasi restock sepatu berdasarkan data penjualan, mendeteksi produk paling diminati, serta membantu pelayanan pelanggan melalui chatbot otomatis.

## 🔄 Penerapan Alur SDLC pada Pipeline CI/CD (GitHub Actions)
Pengembangan sistem ini menerapkan prinsip Software Development Life Cycle (SDLC) secara terstruktur melalui pipa otomatisasi:

1. **Implementation (Git Flow):** Kode program (`main.py`) dikembangkan dan dikirim secara terpusat ke repositori GitHub.
2. **Automated Testing & Quality Gate (CI):** - Robot otomatis menjalankan pengujian (`pytest`) untuk memvalidasi fungsi kecerdasan buatan dalam menghitung rekomendasi restock sepatu serta simulasi API Tukupatu (`test_system.py`).
   - Melakukan *Security Scan* menggunakan `bandit` untuk memastikan keamanan kode dari celah kebocoran data transaksi digital atau *API Keys*.
3. **Deployment (CD):** - Aplikasi siap dibungkus ke dalam **Docker** (menggunakan `Dockerfile`) agar dapat berjalan secara konsisten di lingkungan server staging maupun produksi tanpa kendala perbedaan versi lingkungan (*works on my machine* bugs).

## 🛠️ Perangkat Ekosistem (Tech Stack)
- **CI/CD Orchestrator:** GitHub Actions
- **Containerization:** Docker
- **Programming Language:** Python 3.10
- **Testing Framework:** Pytest
- **Security Audit Tool:** Bandit
