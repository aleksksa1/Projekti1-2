class Funktiot:
    def __init__(self):
        self.luku = None

    def alkuluku(self, luku):
        self.luku = luku
        if luku < 2 or luku % 2 == 0:
            return False

        for i in range(2, luku - 1):
            if luku % i == 0:
                return False

        else:
            return True

