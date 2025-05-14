import os
yol = "C:\\Users\\Administrator\\Desktop"
dosya_yolu =  os.path.join(yol,"deneme.txt")
if os.path.exists(dosya_yolu):
    dosya = open(dosya_yolu,"r")
else:
    dosya = open(dosya_yolu,"x")
    dosya.write("dosya boş")
    dosya.close
    dosya = open(dosya_yolu,"r")

for satir in dosya:
    print(satir)

dosya.close
