# příklad od učitele

class StringBuilder():
    def __init__(self, str=""):
        self.__strings = [str]

    def append(self, new_str):
        self.__strings.append(new_str)
        return self

    def show_data(self):
        print(self.__strings)
    def build(self):
        result = ""
        for str in self.__strings:
            result += " " + str
        return result

sb = StringBuilder("Začatek")
sb.append("prostředek").append("prostředek2")
sb.append("konec.")
sb.show_data()
sentence = sb.build() #vystavení dat v celku
print(sentence)



