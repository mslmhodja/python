# kullanıcıdan bir klasör ismi isteyen
# kullanıcıdan yeni klasörü oluşturacağınız dizinin yolunu isteyen
# bu klasör daha önce varsa ekrana "bu klasör zaten var" şeklinde mesaj veren 
# yoksa bu klasörü verlien yol içerisinde oluşturan program.

import os
yol = input("yeni klasörü oluşturacağınız dizinin yolunu yazınız")
isim = input("yeni klasörün adını yazınız")
if os.path.exists(yol):
    os.chdir(yol)

if os.path.exists(isim):
    print (f"{isim} isimli klasör zaten var")
else:
    sonuc=os.path.join(yol,isim)
    os.mkdir(sonuc)
    print(f"{isim} klasörü oluşturuldu")
