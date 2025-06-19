from ..core.base import Sorun, Cozum, Alan , Kullanici,Yetkili



def alan_bul(x):
    if isinstance(x, int):
        for k in Alan.Alanlar.keys():
            if x == k :
                return Alan.Alanlar[x]
    else:
        for deger in Alan.Alanlar.values():
            if x==deger.konu:
                return deger
            


def sorun_bul(x,y):
    alan1=alan_bul(x)
    if alan1:
        if isinstance(y, int):
            if y <=len(alan1.sorunlar):
                return alan1.sorunlar[y-1]
            else: 
                print("sorun bulunamadı")
         
        else:
            alan1=alan_bul(x)
            for i in alan1.sorunlar:
                if i.problem==y:
                    return i
    else:
        print("Alan bulunamadi")



def cozum_bul(x,y,z):
    sorun=sorun_bul(x,y)
    if isinstance(z, int):
        for i in sorun.cozumler:
            if z==i.id:
                return i #çozum nesnenini döndür



def Kullanici_bul(x):
    for i in Kullanici.tum_kullanicilar:
        if  x==i.Adress:
            return i 



def Yetkili_bul(x):
    for i in Yetkili.tum_yetkililer:
        if x==i.Adress:
            return i
        

def yetkili_kontrol(adress):
    if adress not in [k.Adress for k in Yetkili.tum_yetkililer]:
        return False
    else:
        return True



def kullanici_kontrol(adress):
    if adress not in [k.Adress for k in Kullanici.tum_kullanicilar]:
        return False
    else:
        return True
