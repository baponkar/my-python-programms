

class Duck(object):
    def __init__(self,input_name):
        self._name = input_name


        @property
        def name(self):
            print("Inside the getter")
            return self._name


        @name.setter
        def name(self, input_name):
            print("Inside the setter")
            self._name = input_name

a = Duck("abc")
print(a.name)

#fowl = Duck('Howard') 
#print(fowl.name)


#fowl.name = 'Daffy'
#print(fowl.name)
