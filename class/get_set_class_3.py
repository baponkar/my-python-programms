#My new try in get set class


class Element(object):

    def __init__(self,name):
        self.name = str(name)
        self.__symbol = self.name[0].upper()
        print("Inside of __init__")

    @property
    def symbol(self):
        print("inside of getter")
        return self.__symbol

    @symbol.setter
    def symbol(self,val):
        print("Inside of setter")
        self.__symbol = val


hydrogen = Element("Hydrogen")
print(hydrogen.name)
print(hydrogen.symbol)

hydrogen.symbol = "CL"

print(hydrogen.symbol)
