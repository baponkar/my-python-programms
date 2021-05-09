import ex1

#data = attributes, function = method

class Thing2():
    def __init__(self, val):
        self.letters = val

thing2 = Thing2('abc')
print(thing2.letters)


class Element():
    def __init__(self,name,symbol,number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def dump(self):
        print(self.name,self.symbol,self.number)


data = {'name' : 'Hydrogen','symbol' : 'H','number' : 1}

hydrogen = Element(data['name'],data['symbol'],data['number'])

print(hydrogen.name)

print(hydrogen.dump())

print(hydrogen)

class NewElement():
    def __init__(self,name,symbol,number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def __str__(self):
        print(self.name,self.symbol,self.number)
        return "None"
new_hydrogen = NewElement('Hydrogen','H',1)

print(new_hydrogen)

