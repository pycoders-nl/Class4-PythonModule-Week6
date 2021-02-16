class Dikdortgen:
    def __init__(self,uzun_kenar,kisa_kenar):
        self.uzun_kenar=uzun_kenar
        self.kisa_kenar=kisa_kenar
    def alan(self):
        return self.uzun_kenar*self.kisa_kenar
    def cevre(self):
        return (self.uzun_kenar+self.kisa_kenar)*2
d_uzunkenar=int(input('Dikdortgenin uzun kenar olcusunu giriniz...:'))
d_kisakenar=int(input('Dikdortgenin kisa kenari olcusunu giriniz....:'))
dikdortgen=Dikdortgen(d_uzunkenar,d_kisakenar)
print('Dikdortgenin Alani......:',dikdortgen.alan())
print('Dikdortgenin Cevresi....:',dikdortgen.cevre())

class Kare(Dikdortgen):
    def __init__(self,uzun_kenar):
        super().__init__(uzun_kenar,uzun_kenar)
    def alan(self):
        return self.uzun_kenar**2
    def cevre(self):
        return self.uzun_kenar*4
k_kenar=int(input('Karenin kenar olcusunu giriniz...:'))
kare_=Kare(k_kenar)
print('Karenin alani...:',kare_.alan())
print('Karenin cevresi.:',kare_.cevre())
class kup(Kare):
    def __init__(self,uzun_kenar) -> object:
        self.uzun_kenar=uzun_kenar
    def alan(self):
        return 6*self.uzun_kenar*self.uzun_kenar
    def hacim(self):
        return self.uzun_kenar*self.uzun_kenar*self.uzun_kenar
kup_kenar=int(input('Kupun kenar olcusunu giriniz...:'))
kup_=kup(kup_kenar)
print('Kupun Alani....:',kup_.alan())
print('Kupun Hacmi...:',kup_.hacim())
class ucgen:
    def __init__(self,taban,yukseklik):
        self.taban=taban
        self.yukseklik=yukseklik
    def alan (self):
        return self.taban*self.yukseklik/2
    def cevre(self):
        return self.taban*self.yukseklik*self.taban
ucgen_taban=int(input('Eskenar ucgenin bir kenar olcusunu giriniz...:'))

ucgen_=ucgen(ucgen_taban,ucgen_taban)
print('Es Kenar Ucgenin Alani...:',ucgen_.alan())
print('Es Kenar Ucgenin Cevresi...:',ucgen_.cevre())

