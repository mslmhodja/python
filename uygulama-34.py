# Syntax : datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0) 
# Returns : Date
#

from datetime import datetime, timedelta
import locale

locale.setlocale(locale.LC_ALL, 'tr_TR.utf8')
bugun = datetime.today()
ekleme = timedelta(weeks=18, hours=4)
sonuc = bugun + ekleme

# bugünün tarihini Çarşamba, 12 Mart 25, 02:26 ÖS
#şeklinde yazdıran kod

print(bugun.strftime("%A, %d %B %y, %I:%M %p"))
print(ekleme)
print(sonuc.strftime('%d.%m.%Y %A'))




# kullanıcının verdiği tarihi tarih formatına dönüştürme.
# datetime.strptime(degisken,"%d.%m.%Y %A")
from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, 'tr_TR.utf8')


tarih = input("lütfen tarihi 15 ocak 2025 şeklinde türkçe gir.")
print(datetime.strptime(tarih,"%d %B %Y"))
