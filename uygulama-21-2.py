for x in range(101):
  if not(x>50 and x<=70):
    print(x)

print("çıkmak için 999 yaz")
ort = int(input("ortalaman kaç"))
while (ort!=999) :    
    if ort<0:
        print("geçersiz not")
    elif ort<20 and ort>=0:
        print("E")
    elif ort<50 and ort>=20:
        print("D")
    elif ort<70 and ort>=50:
        print("C")
    elif ort<85 and ort>=70:
        print("B")
    elif ort<=100 and ort>=85:
        print("A")
        if ort==100:
            print("Adamsın. mükemmelsin")
    else:
        print("geçersiz not")
    ort = int(input("ortalaman kaç"))
print("güle güle")
