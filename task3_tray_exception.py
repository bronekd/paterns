#Úkol 3
#Uživatel zadá číslo měsíce (od 1 do 12). Na základě zadaného čísla program zobrazí jedno z následujících: Zima, pokud je číslo 1, 2 nebo 12, Jaro, pokud je číslo v rozsahu od 3 do 5, Léto, pokud je od 6 do 8, Podzim, pokud je od 9 až 11.
#Pokud je číslo mimo rozsah, zobrazí se chybová zpráva.
class WrongMonthError(Exception):
    def __init__(self, message="Cannot update state beyond the final state."):
        self.message = message
        super().__init__(self.message)

try:
    month = int(input("Zadej číslo měsíce od 1 do 12: "))

    if month not in range(1, 13):
        raise WrongMonthError

    if month < 1 or month > 12:
        print("Zadal jsi špatné číslo takový měsíc nemáme ")
    elif month in [1, 2, 12]:
        print("Zadal jsi měsíc zima.")
    elif month >= 3 and month <= 5:
        print("Zadal jsi měsíc léta.")
    elif month >= 6 and month <= 8:
        print("Zadal jsi měsíc léta.")
    elif month >= 9 and month <= 11:
        print("Zadal jsi měsíc léta.")
except ValueError:
    print("Nezadal jsi číslo")

except WrongMonthError:
    print("Zadal jsi číslo mimo rozsah")


"""
def season(num):
    if num < 1 or num > 12:
        print("Zadal jsi špatné číslo takový měsíc nemáme ")
    elif num in [1, 2, 12]:
        print("Zadal jsi měsíc zima.")
    elif num >= 3 and num <= 5:
        print("Zadal jsi měsíc léta.")
    elif num >= 6 and num <= 8:
        print("Zadal jsi měsíc léta.")
    elif num >= 9 and num <= 11:
        print("Zadal jsi měsíc léta.")

input_season_number = input("Zadej číslo měsíce od 1 do 12: ")
season(input_season_number)


if input_season_number > 12:
    raise Exception("Sorry, OU NOOOOO")
elif input_season_number < 1:
    raise Exception("No to je málo.")
"""




