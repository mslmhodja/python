# iki sayı arasındaki sayıların karelerinin toplamını bulan fonksiyon
def ntoplam(bas,bit):
    toplam=0
    for n in range(bas,bit+1):
        toplam+= n*n
    return toplam

print(ntoplam(8,12))

# uç sayıyı parametre olarak alan,
# bunların en büyüğünü bulan
# geriye bulduğu sayıyı döndüren fonksiyon

def enbuyuk(a,b,c):
    if a>b and a>c :
        return a
    if b>c and b>a :
        return b
    if c>b and c>a :
        return c

print("en büyük ",enbuyuk(3,9,2))
