# test_system.py
from main import hitung_rekomendasi_restock, cek_koneksi_api_tukupatu

def test_fitur_restock_ai():
    # Tes apakah robot pintar benar merekomendasikan restock jika stok sisa 2
    hasil = hitung_rekomendasi_restock(stok_sekarang=2, total_penjualan=10)
    assert hasil == "Rekomendasi: Segera Restock Sepatu!"

def test_integrasi_api():
    # Tes apakah sistem bisa terhubung ke marketplace
    assert cek_koneksi_api_tukupatu() == "Terhubung ke Tukupatu"