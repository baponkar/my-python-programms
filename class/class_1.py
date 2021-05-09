#simple class

class Person():
    def __init__(self,name):
        self.name = name


bapon = Person('bapon')

print(bapon.name)



#setter and getter

class NewPerson():
    def __init__(self,input_name):
        self.hidden_name = input_name
        print("a new person class created")

 
    def name_getter(self):
        print("Inside of getter")
        return self.hidden_name
    
    def name_setter(self, input_name):
        print("Inside the setter")
        self.hidden_name = input_name
    
    name = property(name_setter,name_getter)

bittu = NewPerson("Bittu")
#print(bittu.hidden_name)
class_name = bittu.name
print(class_name)

bittu.name_setter = 'raju'

#print(bittu.name)

