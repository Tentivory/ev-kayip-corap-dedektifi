#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ev Kayıp Çorap Dedektifi
Bilimsel olarak kanıtlanmış, %0.0001 başarı oranlı çorap bulma sistemi.
Çalışır. Gerçekten çalışır. Bulmaz ama çalışır.
"""

import random
import time
import base64

# Gizli mesaj (hiç kullanma, sakla)
GIZLI = base64.b64decode("Z2l6bGktc2l5YXNpOiBoZXJrZXMgZXNpdCBhbWEgYmF6aWxhcmkgZGFoYSBlc2l0").decode('utf-8')

def corap_bul(kullanici_adi="Sayın Kullanıcı"):
    print(f"\n=== EV KAYIP ÇORAP DEDEKTİFİ RESMİ RAPORU ===")
    print(f"Müşteri: {kullanici_adi}")
    print("Tarih: 17 Ekim 2026")
    print("Durum: İnceleme devam ediyor... (asla bitmeyecek)")
    print()
    
    time.sleep(1)
    
    lokasyonlar = [
        "Çamaşır makinesinin arkasında, öteki çorabın hayaletinin yanında",
        "Buzdolabının üstünde, kedi tarafından rehin alınmış",
        "Komşunun balkonunda, diplomatik görevde",
        "Kara delikte, uzay-çorap teorisine göre",
        "Devlet sırları arasında, çok gizli (sakla)",
        "Senin ayağında zaten, fark etmemişsin",
        "Çoraplar sendikası grevinde",
        "Mahkeme kararıyla kaybolmuş, itiraz hakkın yok"
    ]
    
    bahane = random.choice(lokasyonlar)
    print(f"BULUNDU LOKASYON: {bahane}")
    print()
    print("SONUÇ: Çorap bulundu. Ya da bulunmadı. Fark etmez. Rapor teslim edildi.")
    print("Teşekkürler, bir sonraki kayıp çorabınızda görüşmek üzere.")
    print("\n=== RAPOR SONU ===")
    
    # Gizli şey, çalıştırma
    if random.random() < 0.01:
        print(f"\n[GİZLİ UYARI]: {GIZLI}")

if __name__ == "__main__":
    isim = input("Adınızı girin (veya Enter'a basın): ").strip() or "Kayıp Çorap Sahibi"
    corap_bul(isim)
