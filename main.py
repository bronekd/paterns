# Vytvořit builder na nějaké vlastní aplikaci.

class Order:
    def __init__(self, jmeno, mesto, ulice, psc):
        self.jmeno = jmeno
        self.mesto = mesto
        self.ulice = ulice
        self.psc = psc

class OrderBuilder:
    def __init__(self):
        self.jmeno = None
        self.mesto = None
        self.ulice = None

    def nastav_jmeno(self, jmeno):
        self.jmeno = jmeno
        return self

    def nastav_mesto(self, mesto):
        self.mesto = mesto
        return self

    def nastav_ulice(self, ulice):
        self.ulice = ulice
        return self

    def nastav_psc(self, psc):
        self.psc = psc
        return self


    def build(self):
        return Order(self.jmeno, self.mesto, self.ulice, self.psc)


builder = OrderBuilder()
my_adresa = (builder.nastav_jmeno("Jmeno")
             .nastav_mesto("Octavia")
             .nastav_ulice("ulice")
             .nastav_psc(12358)
             .build())

print(my_adresa.jmeno, my_adresa.mesto, my_adresa.ulice, my_adresa.psc)