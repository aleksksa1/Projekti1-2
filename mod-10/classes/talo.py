from classes.hissi import Hissi

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissien_lkm = hissien_lkm
        self.hissit = []
        for i in range(hissien_lkm):
            self.hissit.append(Hissi(self.alin_kerros, self.ylin_kerros))


    def aja_hissia(self, hissin_numero, kohde):
        print("-----------------")
        print(f"Ajat hissillä: {hissin_numero}")
        self.hissit[hissin_numero - 1].siirry_kerrokseen(kohde)
        print("-----------------")


    def tulipalo(self):
        for i in range(len(self.hissit)):
            self.aja_hissia(i + 1, 1)

