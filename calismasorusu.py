# Fonksiyon: Not ortalaması hesapla
def ortalama_hesapla(n1, n2):
    return (n1 + n2) / 2

# Fonksiyon: Geçti mi kaldı mı?
def gecti_mi(ortalama):
    return "Geçti" if ortalama >= 50 else "Kaldı"

# Fonksiyon: Öğrenci ekle
def ogrenci_ekle(ogrenciler):
    ad = input("Öğrenci adı: ")
    try:
        not1 = float(input("1. sınav notu: "))
        not2 = float(input("2. sınav notu: "))
        ort = ortalama_hesapla(not1, not2)
        durum = gecti_mi(ort)
        ogrenciler.append((ad, not1, not2, ort, durum))
        print(f"{ad} eklendi. Ortalama: {ort:.2f} → {durum}")
    except:
        print("⚠️ Geçersiz not girdiniz!")

# Fonksiyon: Öğrenci listesini göster
def ogrencileri_goster(ogrenciler):
    if not ogrenciler:
        print("Henüz öğrenci eklenmedi.")
    else:
        print("\n📋 Öğrenci Listesi:")
        for ogr in ogrenciler:
            print(f"→ {ogr[0]} - Not1: {ogr[1]}, Not2: {ogr[2]}, Ort: {ogr[3]:.2f}, Durum: {ogr[4]}")

# Fonksiyon: Dosyaya kaydet
def dosyaya_kaydet(ogrenciler):
    try:
        dosya = open("notlar.txt", "w", encoding="utf-8")
        for ogr in ogrenciler:
            satir = f"{ogr[0]} - Not1: {ogr[1]}, Not2: {ogr[2]}, Ort: {ogr[3]:.2f}, Durum: {ogr[4]}\n"
            dosya.write(satir)
        dosya.close()
        print("✅ Bilgiler 'notlar.txt' dosyasına kaydedildi.")
    except:
        print("⚠️ Dosya yazma hatası")

# Fonksiyon: Dosyadan oku ve verileri listeye aktar
def dosyadan_oku(ogrenciler):
    try:
        dosya = open("notlar.txt", "r", encoding="utf-8")
        satirlar = dosya.readlines()
        dosya.close()

        if not satirlar:
            print("❗ Dosya boş. Henüz öğrenci kaydedilmemiş.")
            return

        ogrenciler.clear()  # Listeyi temizle
        print("\n📄 Dosyadaki Öğrenciler:")
        for satir in satirlar:
            print(f"→ {satir.strip()}")
            try:
                parcalar = satir.strip().split(" - ")
                ad = parcalar[0]
                diger = parcalar[1].split(", ")
                not1 = float(diger[0].split(": ")[1])
                not2 = float(diger[1].split(": ")[1])
                ort = float(diger[2].split(": ")[1])
                durum = diger[3].split(": ")[1]
                ogrenciler.append((ad, not1, not2, ort, durum))
            except (IndexError, ValueError):
                print("⚠️ Satırdan veri ayrıştırılamadı!")
    except:
        print("❗ Dosya bulunamadı. Önce kaydetmelisiniz.")

# Ana Menü Fonksiyonu
def menu():
    ogrenciler = []

    while True:
        print("\n📌 MENÜ")
        print("1 - Öğrenci Ekle")
        print("2 - Öğrencileri Göster")
        print("3 - Dosyaya Kaydet")
        print("4 - Dosyadan Oku ve Listeye Aktar")
        print("0 - Çıkış")

        secim = input("Bir seçenek girin (0-4): ")

        if secim == '1':
            ogrenci_ekle(ogrenciler)
        elif secim == '2':
            ogrencileri_goster(ogrenciler)
        elif secim == '3':
            dosyaya_kaydet(ogrenciler)
        elif secim == '4':
            dosyadan_oku(ogrenciler)
        elif secim == '0':
            print("👋 Programdan çıkılıyor...")
            break
        else:
            print("⚠️ Geçersiz seçim! Lütfen 0-4 arasında bir sayı girin.")

# Programı çalıştır
menu()
