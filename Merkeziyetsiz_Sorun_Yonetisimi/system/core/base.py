
class Kullanici:
    tum_kullanicilar = []

    id=0
    def __init__(self,Adress, puan=0):
        self.Adress = Adress
        self.id=Kullanici.id
        self.puan=puan
        Kullanici.id+=1
        Kullanici.tum_kullanicilar.append(self)
       
class Yetkili(Kullanici):
    tum_yetkililer = []

    def __init__(self, Adress):
        super().__init__(Adress)
        
        self.rol = "Yetkili"
        Yetkili.tum_yetkililer.append(self)


    def to_dict(self):
      pass  

class Alan:
    Alanlar={}
    id_sayac = 0

    def __init__(self, Adress, Alan_adi,Guven_tabakasi=None):
        if Guven_tabakasi:
            if len(Guven_tabakasi)>=3:
                self.asama=1
                self.tabaka=Guven_tabakasi
            else:
                self.asama=0
        else :
            self.asama=0
       
        

        self.id = Alan.id_sayac
        Alan.id_sayac += 1

        self.yetkili = Adress
        self.konu = Alan_adi
        self.sorunlar = []
        self.sorun_id_sayac = 1  # her alanda 1’den başlar
        Alan.Alanlar[self.id] = self
        


    def sorun_ekle(self, problem, adres):
        s = Sorun(self.sorun_id_sayac, self, problem, adres)
        self.sorun_id_sayac += 1
        self.sorunlar.append(s)
        return s
 


    def to_dict(self):
        pass


class Sorun:
    
    def __init__(self, id, alan : Alan, problem, adres):
        self.id = id  # bu id sadece alan içinde geçerli
        self.asama=0 
        self.alan = alan#ait olduğu alanın sınıfını döndürür
        self.problem = problem
        self.sahip = adres
        self.degerlendirme=[]
        self.cozumler = []
        self.cozum_id_sayac = 1
        self.onay=False 
        self.asama=0

    def cozum_ekle(self, icerik, adres):
        if  self.onay and self.asama==1:
            c = Cozum(self.cozum_id_sayac, self, icerik, adres)
            self.cozum_id_sayac += 1
            self.cozumler.append(c)
            return c
        else:
            print("SORUN \n Cozum ekleme aşamasında Değil")
            return False

    def to_dict(self):
        pass


class Cozum:
    def __init__(self, id, sorun, icerik, adres):
        self.id = id  # bu id sadece sorun içinde geçerli
        self.onay=False #güven_tabakasi onayı // training-wheels 
        self.sorun = sorun
        self.icerik = icerik
        self.sahip = adres
        self.degerlendirmeler = []
        self.yildizlar=[]

    def cozum_degerlendir(self,yildiz,adress):
        self.yildizlar.append({adress:yildiz})

    def to_dict(self):
        pass
      
        

