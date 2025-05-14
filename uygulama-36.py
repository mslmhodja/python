
sonuc=5
while sonuc!=0:
  try:
    s1 = int(input("1.sayıyı gir"))
    s2 = int(input("2.sayıyı gir"))  
    sonuc = s1/s2
    print(f"sonuç={sonuc}")
  except:
    print("hatalı rakam girişi yaptınız")
  
  
