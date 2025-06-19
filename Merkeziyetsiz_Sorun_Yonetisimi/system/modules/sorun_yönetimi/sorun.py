from textwrap import dedent

from ...core.base import Sorun, Cozum,Alan,Kullanici
from ..araci_yonetim import *


def sorun_olustur(Adress,alan,icerik):
    a=alan_bul(alan)
    if a:
        if a.asama==1:
            s=a.sorun_ekle(icerik,Adress)
            #print(f"####################################\nSorun olusturldu\nicerik\n{s.problem}\nsorun id  {s.id}\nalan id {a.id}\nalan konusu {a.konu}\nsorun asamasi {s.asama}\nCozum öneri sayisi {len(s.cozumler)}\n Sorun degerlendirme sayisi {len(s.degerlendirme)} \n####################################")
            print(dedent(f"""
        ─────────────────────────────────────────
        🆘 Sorun oluşturuldu
        • İçerik              : {s.problem}
        • Sorun ID            : {s.id}
        • Alan ID / Konu      : {a.id} / {a.konu}
        • Aşama               : {s.asama}
        • Çözüm önerisi       : {len(s.cozumler)}
        • Değerlendirme adedi : {len(s.degerlendirme)}
        ─────────────────────────────────────────
    """).strip())
        else:
            print("Sorun olusturulamadi\n Alan aktif değil")
            
        

    else:
        print("ALAN MEVCUT DEĞİL")


def sorun_degerlendir(alan,sorun,adress,tercih):
    a=alan_bul(alan)
    s=sorun_bul(alan,sorun)
    if s and s.asama==0 and len(a.tabaka) >= 3:
        if adress in a.tabaka:
            s.degerlendirme.append((adress, tercih))  # Oy ekleniyor

            if len(s.degerlendirme) >= int(len(a.tabaka) * 3 / 4):  # %75 oranına ulaşıldıysa
                k = {0: 0, 1: 0}  # Tercih sayacı
                for _, t in s.degerlendirme:
                    if t in k:
                        k[t] += 1
                        
                k1=Kullanici_bul(s.sahip)
                
                # Çoğunluk hangisiyse onu döndür
                if k[1]>k[0]:
                    s.asama+=1
                    s.onay=True
                    print(dedent(f"""
            ─────────────────────────────────────────
            ✅  SORUN ASAMA ATLADI VE ÖDÜL VERİLDİ 
            • Gerekli güven tabakasi onayina ulaştı
            • Sorun ID            : {s.id}
            • Alan ID / Konu      : {a.id} / {a.konu}
            • Sorun asama         :  {s.asama}
            •  Sorun sahibi 
                        {k1.Adress}
                                
            
            
            ─────────────────────────────────────────
        """).strip())
                    k1.puan +=10

                else:
                    print(dedent(f"""
            ─────────────────────────────────────────
             ❌  SORUN  REDDEDİLDİ 
            • Sorun Güven tabakasi tarafından reddedildi VE sorun sahibine ceza verildi -10 puan
            • Sorun ID            : {s.id}
            • Alan ID / Konu      : {a.id} / {a.konu}
            •  Sorun sahibi 
                        {k1.Adress}
                                
            
            
            ─────────────────────────────────────────
        """).strip())
                    
                    k1.puan-=10
            else:
                onay = "Onay verildi" if tercih else "Reddedildi"

                print(dedent(f"""
            ─────────────────────────────────────────
            ✅  SORUN BAŞARIYLA DEĞERLENDİRİLDİ
            • Alan       : {a.konu} / {a.id}
            • Sorun ID   : {s.id}
            • Tercih     : {onay}
            ─────────────────────────────────────────
        """).strip())
        
                
                    
    else:
        print("Sorun Degerlendirme asamasında değil")

# def sorun_asama_yonetimi(alan,sorun):

#     pass
        
#     print("SORUN basarıyla degerlendirildi")


    
