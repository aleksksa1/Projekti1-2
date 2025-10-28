from classes.julkaisu import Julkaisu
from classes.julkaisu import Lehti
from classes.julkaisu import Kirja

julkaisu1 = Lehti("Aku ankka", "Aki Hyyppä")
julkaisu2 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)


julkaisu1.tulosta_tiedot()
julkaisu2.tulosta_tiedot()