class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.kerros = alin_kerros
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros


    def kerros_ylos(self):
        self.kerros += 1
        print(f"Kerros: {self.kerros}")


    def kerros_alas(self):
        self.kerros -= 1
        print(f"Kerros: {self.kerros}")


    def siirry_kerrokseen(self, new_kerros):
        print(f"Kerros: {self.kerros}")
        while new_kerros != self.kerros:
            if self.kerros < new_kerros:
                Hissi.kerros_ylos(self)

            elif self.kerros > new_kerros:
                Hissi.kerros_alas(self)

