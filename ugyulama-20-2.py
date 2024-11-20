# okul 
#	okulno, adı, ili, ilçesi, öğrenci sayısı, öğretmen sayısı, türü, kuruluş yılı
    
okul = {
  "okulno":0,
  "adi" : "",
  "ili":"",
  "ilcesi":"",
  "ogrencisayisi":0,
  "ogretmensayisi":0,
  "türü":"",
  "kurulus":0
}

okul["okulno"] = input("Okul No Giriniz: ")
okul["adi"] = input("Okulun Adını Giriniz: ")
okul["ili"] = input("Okul İlini Giriniz: ")
okul["ilcesi"] = input("Okulun İlcesi: ")
okul["ogrencisayisi"] = input("Okul ogrenci sayisinı Giriniz: ")
okul["ogretmensayisi"] = input("Okul ogretmen sayisinı Giriniz: ")
okul["türü"] = input("Okul Türünü Giriniz: ")
okul["kurulus"] = input("Okul Kuruluş Yılını Giriniz: ")


print ("Okul No" , okul["okulno"])
print ("Okul Adı: " , okul["adi"])
print ("Okulun İli", okul["ili"])
print ("Okulun İlcesi", okul["ilcesi"])
print ("Okulun Ögrenci Sayisi", okul["ogrencisayisi"])
print ("Okulun Ögretmen Sayisi", okul["ogretmensayisi"])
print ("Okulun türü", okul["türü"])
print ("Okulun kurulus Yılı", okul["kurulus"])
