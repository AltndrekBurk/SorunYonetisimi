from ...core.base import Alan
from ..araci_yonetim import yetkili_kontrol,kullanici_kontrol        
from textwrap import dedent

# admin = Yetkili("0x000000000") #Adressi ile giriş yapar beyaz listede ise 
# a1 = Alan.olustur(admin, "Fizik")
def alan_olustur(Adress, alan_adi,Guven_tabakasi):#DİKKAT güven-tabakasi liste olarak alınacak
    alan=None
    
    if yetkili_kontrol(Adress): #Adress yetkili ise Alan olusturabilsin
        alan = Alan(Adress=Adress, Alan_adi=alan_adi,Guven_tabakasi=Guven_tabakasi)
        
        #print(f"###########ALAN OLUSTURULDU####################\nalan id : {alan.id} \nalan konusu  {alan.konu}  \nalan asamsi {alan.asama} \n***Alan yetkili adresi  {alan.yetkili}***\n####################################")
        
        guven_str = ", ".join(Guven_tabakasi) if Guven_tabakasi else "None"
        print(dedent(f"""
        ─────────────────────────────────────────
        🗂️  ALAN OLUŞTURULDU
        • ID            : {alan.id}
        • Konu          : {alan.konu}
        • Aşama         : {alan.asama}
        • Yetkili Adres : {alan.yetkili}
        • Atanan güven tabakasi : {guven_str}
        ─────────────────────────────────────────
    """).strip())

    else:
        print("Alan olusturma yetkiniz yok")
        # guven_tabakasi başlangıç admin tarafından belirlenebilir
#alan nesnesini döndürür
