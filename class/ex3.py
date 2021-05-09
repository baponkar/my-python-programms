class Element(object):
    def __init__(self,name,symbol,number):
        self.__name = name
        self.__symbol =symbol
        self.__number = number


        @property
        def data(self):
            print("Inside the getter")
            return {self.__name,self.__symbol,self.__number}

        @data.setter
        def data(self,name,symbol,number):
            print("Inside setter")
            self.__name = name
            self.__symbol = symbol
            self.__number = number

        #data = property(get_data,set_data())
hydrogen = Element("Hydrogen","H",1)

print(hydrogen.data)
#print(hydrogen.name)
