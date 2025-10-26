from classes.auto10 import Auto

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot
        self.aika = 0

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kulje(1)
        self.aika = self.aika + 1
        if self.aika % 10 == 0:
            self.tulosta_tilanne()

    def tulosta_tilanne(self):
        print(f"Tilanne {self.aika} tunnin jälkeen:")
        for auto in self.autot:
            print(auto.ominaisuudet())

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka >= self.pituus:
                print(f"{self.nimi} on ohi!")
                self.tulosta_tilanne()
                return True
        return False