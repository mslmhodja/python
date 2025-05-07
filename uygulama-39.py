# aşağıdaki gibi bir menü oluştur
#klasör değiştir................1
#klasör oluştur................2
#klasörü sil................3
#klasör adını değiştir................4
#aktif klasörü göster................5
#çıkış................0
#menüyü döngüye al
#verilenseçenek numarasına göre işlem yap
#her işlem için bir fonksiyon tanımla

import os  
  
def klasor_degistir():  
    klasor = input("Değiştirmek istediğiniz klasör yolunu girin: ")  
    if os.path.exists(klasor):  
        os.chdir(klasor)  
        print(f"Aktif klasör: {os.getcwd()}")  
    else:  
        print("Klasör bulunamadı.")  
  
def klasor_olustur():  
    klasor = input("Oluşturmak istediğiniz klasörün adını girin: ")  
    if not os.path.exists(klasor):  
        os.mkdir(klasor)  
        print(f"{klasor} klasörü oluşturuldu.")   
    else:  
        print("Klasör zaten var.")  

  
def klasoru_sil():  
    klasor = input("Silmek istediğiniz klasörün adını girin: ")  
    if os.path.exists(klasor):  
        os.rmdir(klasor)  
        print(f"{klasor} klasörü silindi.")   
    else:  
        print("Klasör bulunamadı.")  
    
  
def klasor_adini_degistir():  
    eski_ad = input("Eski klasör adını girin: ")  
    yeni_ad = input("Yeni klasör adını girin: ") 
    if os.path.exists(eski_ad) and (not os.path.exists(yeni_ad)) :  
        os.rename(eski_ad, yeni_ad)  
        print(f"{eski_ad} klasörü {yeni_ad} olarak değiştirildi.")    
    else:  
        print("Klasör adı değiştirilemez.")  
    
 
  
def aktif_klasoru_goster():  
    print(f"Aktif klasör: {os.getcwd()}")  
  
def menu():  
    while True:  
        print("\nMenü:")  
        print("Klasör değiştir................1")  
        print("Klasör oluştur................2")  
        print("Klasörü sil....................3")  
        print("Klasör adını değiştir.........4")  
        print("Aktif klasörü göster...........5")  
        print("Çıkış..........................0")  
          
        secim = input("Seçiminizi yapın: ")  
        try:  
            if secim == '1':  
                klasor_degistir()  
            elif secim == '2':  
                klasor_olustur()  
            elif secim == '3':  
                klasoru_sil()  
            elif secim == '4':  
                klasor_adini_degistir()  
            elif secim == '5':  
                aktif_klasoru_goster()  
            elif secim == '0':   
                break  
            else:  
                print("Geçersiz seçim, lütfen tekrar deneyin.")  
        except:
            print("bir hata oluştu")

menu()  

