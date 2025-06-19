from ...core.base import Kullanici,Yetkili
from textwrap import dedent

GREEN = "\033[92m"   
RESET = "\033[0m"

def kullanici_olustur(adress):

    if adress not in [k.Adress for k in Kullanici.tum_kullanicilar]:
        Kullanici(Adress=adress)
        print(
        dedent(f"""
            ─── KULLANICI OLUŞTURULDU ───
            Adres : {adress}
        """).strip()
    )



def Yetkili_olustur(adress):
    if adress not in [k.Adress for k in Yetkili.tum_yetkililer]:
        Yetkili(Adress=adress)
        print(
        dedent(f"""
            ─── YETKİLİ OLUŞTURULDU ───
            Adres : {adress}
        """).strip()
    )

    else:
        print("Yetkili mevcut")
        
        