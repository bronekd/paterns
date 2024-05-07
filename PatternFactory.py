#factory vytváří objekty nové které potřebuji. Po čas běhu aplikace vytvoří nový obárzek a button v UI. Nebo i v databázi.


class Vozidlo:
    def start(self):
        raise NotImplementedError("Tato metoda musí být přepsána.")

class Auto(Vozidlo):
    def start(self):
        return "Auto startuje"

class Nakladak(Vozidlo):
    def start(self):
        return "Náklaďák startuje"

class Autobus(Vozidlo):
    def start(self):
        return "Autobus startuje"

# tady by šel použit enum protoŽe
# #tady mmam výčet nejakych objektu
class VozidloFactory:
    @staticmethod
    def get_vozidlo(typ):
        if typ == "auto":
            return Auto()
        elif typ == "nakladak":
            return Nakladak()
        elif typ == "autobus":
            return Autobus()
        else:
            raise ValueError("Neznámý typ vozidla")

a = VozidloFactory.get_vozidlo("auto")
n = VozidloFactory.get_vozidlo("nakladak")

print(a.start())
print(n.start())







