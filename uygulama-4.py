# verilen 4 basamaklı sayının basamaklarındaki rakamları bulan kodu yazınız

# a=5879  
# a4 = int (a /1000)) binler basamağını verir
# a3 =                yüzler basamağını verir
# a2 =                onlar basamağını verir
# a3 =                birler basamağını verir

# 1
# 4
# 5
# 8
sayi = 9114
b4 = int(sayi / 1000)
b3 = int(sayi / 100 - b4 * 10)
b2 = int(sayi / 10 - b4 * 100 - b3 * 10)
b1 = int(sayi / 1 - b4 * 1000 - b3 * 100 - b2 * 10)
print(b4)
print(b3)
print(b2)
print(b1)
