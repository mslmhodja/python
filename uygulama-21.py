print("çıkmak için 999 yaz")
ort = int(input("ortalaman kaç"))
while ort!=999:    
    if ort<0:
        print("geçersiz not")
    elif ort <=20:
        print("E")
    elif ort <50:
        print("D")
    elif ort <70:
        print("C")
    elif ort <85:
        print("B")
    elif ort <=100:
        print("A")
        if ort==100:
            print("Adamsın. mükemmelsin")
    else:
        print("geçersiz not")
    ort = int(input("ortalaman kaç"))
print("güle güle")
