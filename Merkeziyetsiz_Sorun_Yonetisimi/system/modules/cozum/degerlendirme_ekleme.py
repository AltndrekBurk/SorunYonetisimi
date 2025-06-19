from ..araci_yonetim import * 
from textwrap import dedent

def cozum_ekle(alan,sorun,icerik,adress):
    a=alan_bul(alan)
    k=Kullanici_bul(adress)
    s=sorun_bul(alan,sorun)
    if s and k and s :
        c=s.cozum_ekle(icerik,adress)
        if c:
            print(dedent(f"""
            ─────────────────────────────────────────
            ✅  COZUM BASARIYLA EKLENDİ
            • Alan       : {a.konu} / {a.id}
            • Sorun ID   : {s.id}
            • COZUM ID   : {c.id}
            • COZUM ONAYI: {c.onay} 

            • önizleme     : {c.icerik}
            ─────────────────────────────────────────
        """).strip())
    else:
        print(dedent(f"""
            ─────────────────────────────────────────
             ❌  COZUM  REDDEDİLDİ 
                 SİSTEMİ KONTROL EDİN VE TEKRAR DENEYİN
            ─────────────────────────────────────────
        """).strip())

def cozum_onayi(alan,sorun,cozum,adress,tercih):
    a=alan_bul(alan)
    s=sorun_bul(alan,sorun)
    c=cozum_bul(alan,sorun,cozum)
    if c and s and s.asama==1 and len(a.tabaka) >= 3:
        if adress in a.tabaka:
            c.degerlendirmeler.append((adress, tercih))  # Oy ekleniyor

            if len(c.degerlendirmeler) >= int(len(a.tabaka) * 1/2):  # %50 oranına ulaşıldıysa
                k = {0: 0, 1: 0}  # Tercih sayacı
                for _, t in c.degerlendirmeler:
                    if t in k:
                        k[t] += 1
                        
                k1=Kullanici_bul(c.sahip)
                
                # Çoğunluk hangisiyse onu döndür
                if k[1]>k[0]:
                    c.onay=True
                    print(dedent(f"""
            ─────────────────────────────────────────
            🏆   COZUM ONAYLANDİ VE ÖDÜL VERİLDİ 
            • Gerekli güven tabakasi onayina ulaştı
            • Sorun ID            : {s.id}
            • Alan ID / Konu      : {a.id} / {a.konu}
            • cozum ID            :  {c.id}
            • Sorun Sahibi        : {c.sorun.sahip}
            • cozum onayi         :  {c.onay}
            •  Cozum sahibi 
                        {k1.Adress}
                                
            
            
            ─────────────────────────────────────────
        """).strip())
                    k1.puan +=4

                else:
                    k1.puan-=4
                    print(dedent(f"""
            ─────────────────────────────────────────
             ❌  COZUM  REDDEDİLDİ 
            • cOZUM Güven tabakasi tarafından reddedildi VE COZUM sahibine ceza verildi -4 puan
            • Sorun ID            : {s.id}
            • Alan ID / Konu      : {a.id} / {a.konu}
            • cozum ID            :  {c.id}
            • Sorun Sahibi        : {c.sorun.sahip}
            • cozum onayi         :  {c.onay}
            •  COZUM sahibi 
                        {k1.Adress}
            
            •  COZUM sahibi güncel puan {k1.puan}                 
            
            
            ─────────────────────────────────────────
        """).strip())
                    
                    
            else:
                onay = "Onay verildi" if tercih else "Reddedildi"

                print(dedent(f"""
            ─────────────────────────────────────────
            ✅  COZUM BAŞARIYLA DEĞERLENDİRİLDİ
            • Alan       : {a.konu} / {a.id}
            • Sorun ID   : {s.id}
            • cozum ID   :  {c.id}
            • Tercih     : {onay}
 
            ─────────────────────────────────────────
        """).strip())
        
                
                    
    else:
        print(dedent(f"""
            ─────────────────────────────────────────
             ❌  COZUM  Değerlendirme amasında değil veya COZUM MEVCUT DEĞİL 
            ─────────────────────────────────────────
        """).strip())


#COZUM DEGERLENDİRME ASAMA 2
#COZUM EKLEME ASAMA 1
def cozum_degerlendir(alan, sorun,cozum,yildiz,adress):
    
    c=cozum_bul(alan,sorun,cozum)
    c.sorun.asama+=1##SİL

    if c.sorun.asama == 2 and adress not in [i.keys() for i in c.yildizlar] and c.onay:
        c.sorun.asama-=1##SİL
        if 0<=yildiz<=10:
            c.cozum_degerlendir(yildiz,adress)
            k2=Kullanici_bul(c.sahip)
            k2.puan+=(2*yildiz-10)
            c_s=Cozumler_degerlendirme_sonuclari(alan,sorun,cozum)
            print(dedent(f"""
            ─────────────────────────────────────────
            ✅  COZUM BAŞARIYLA DEĞERLENDİRİLDİ
            • Alan       : {c.sorun.alan.konu} / {c.sorun.alan.id}
            • Sorun ID   : {c.sorun.id}
            • COZUM ID   : {c.id}

            • Cozume Verilen YİLDİZ     : {yildiz}
            •Cozum sahibi               :  {c.sahip}
            •Cozum sahibinin puani       :  {Kullanici_bul(c.sahip).puan}

            •TOPLAM ALDIĞI YILDIZ       :   {c_s}
            ─────────────────────────────────────────
        """).strip())
            
        else:
            print("girdiğiniz sayi 0-10 arasında olmali")
    else:
        
        if c.sorun.asama==1:
            print(dedent(f"""
            ─────────────────────────────────────────
             ❌  COZUM  DEGERLENDİRME ASAMSINDA DEĞİL 
                isterseniz çözüm ekleyip asama 1 de rol oynayabilirsniz
            ─────────────────────────────────────────
        """).strip())
        else:
            print(dedent(f"""
            ─────────────────────────────────────────
             ❌  COZUM  DEGERLENDİRELEMEDİ 
            ─────────────────────────────────────────
        """).strip())



def Cozumler_degerlendirme_sonuclari(alan,sorun,cozum):
    c=cozum_bul(alan,sorun,cozum)
    if c:
        return sum(sum(d.values()) for d in c.yildizlar)
    else:
        print("COZUM BULUNAMADİ")     