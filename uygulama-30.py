# kullanıcı adı şifre denetimi yapan fonksiyon ve kullanımı
def userControl(user,password):
    if user=="muslimhoca" or password=="1234" :
        return "Geçerli Giriş"
    else:
        return "Geçersiz Giriş"

print(userControl("muslimhoca","3421"))
