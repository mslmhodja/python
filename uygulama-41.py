import os
yol = "C:\\Users\\Administrator\\Desktop"
dosya_yolu =  os.path.join(yol,"sifre.txt")
if os.path.exists(dosya_yolu):
    dosya = open(dosya_yolu,"r")
else:
    dosya = open(dosya_yolu,"x")
    while True:
        kullanici_adi=input("yeni kullanici_adi: ")
        sifre=input("yeni şifre: ")
        if len(kullanici_adi) >3 and len(sifre) >3 :
            break
    
    dosya.write(kullanici_adi+'\n')
    dosya.write(sifre)
    dosya.close
    dosya = open(dosya_yolu,"r")


kullanici_adi=input("kullanici_adi: ")
sifre=input("şifre: ")
d_kul =dosya.readline()
d_sifre=dosya.readline()

if d_kul == (kullanici_adi+'\n') and d_sifre == sifre:
    print("giriş başarılı")
else:
    print("giriş başarısız")
dosya.close

# kullancı ve şifre oluşturulmamış ise 
# bir dosya oluşturup kullanıcıdan kulanıcı adı ve şifreyi alıp kaydetsin.
# değilse kullanıcı adı ve şifre sorup 
# dosyadakiyle karşılaştırarak giriş başarılı yada başarızı yazan program.
