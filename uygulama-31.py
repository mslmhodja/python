
# geçerli kullanıcı adı ve şifre bilgileri tanımlama, birden fazla kullanıcı adı ve şifre bilgisi olsun
g_users = (
    {"user":"muslimhoca", "password":"1234"},
    {"user":"ayku", "password":"234"},
    {"user":"hasna", "password":"23423"},
    {"user":"kadir", "password":"1232523454"},
    {"user":"tayfur", "password":"123423234"}
)

# kullanıcıdan alınan giriş bilgilerini kontrol

kad = input("kullanıcı adınız:")
sifre = input("Şifreniz:")

# tüm kullanıcılar için kullanıcı adı şifre denetimi yapan fonksiyon ve kullanımı
# dönüş değerleri True False olsun.

def userControl(user,password):  
    global g_users  
    for kullanici in g_users:
        if user==kullanici["user"] and password==kullanici["password"] :
            return True            
    return False

print(userControl(kad,sifre))
