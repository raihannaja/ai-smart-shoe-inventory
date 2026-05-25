def hitung_rekomendasi_restock(stok_sekarang, total_penjualan):
    """Fungsi AI untuk mendeteksi apakah toko harus beli sepatu lagi"""
    if stok_sekarang < 5 or total_penjualan > 50:
        return "Rekomendasi: Segera Restock Sepatu!"
    return "Stok Aman"

def cek_koneksi_api_tukupatu():
    """Simulasi integrasi dengan marketplace Tukupatu"""
    return "Terhubung ke Tukupatu"

if __name__ == "__main__":
    print("--- AI Smart Shoe Inventory System Aktif ---")
    print(hitung_rekomendasi_restock(3, 60))