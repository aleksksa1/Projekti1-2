class Auto:
    def __init__(self, new_rekisteritunnus, new_huippunopeus):
        self.rekisteritunnus = new_rekisteritunnus
        self.huippunopeus = new_huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, arvo):
        self.nopeus = self.nopeus + arvo
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, aika):
        self.matka = self.matka + aika * self.nopeus

    def ominaisuudet(self):
        tulos = {"Rekisteritunnus" : self.rekisteritunnus,
                 "Huippunopeus" : self.huippunopeus,
                 "Nopeus" : self.nopeus,
                 "Matka" : self.matka}
        return tulos

class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(rekisteritunnus, huippunopeus)

    def ominaisuudet(self):
        super().ominaisuudet()


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankki):
        self.bensatankki = bensatankki
        super().__init__(rekisteritunnus, huippunopeus)

    def ominaisuudet(self):
        super().ominaisuudet()