class Man(object):

    def __init__(self,name,profesion,degree):
    	self._name = name
    	self.__profesion = profesion
    	self.__degree = degree
    	
    @property
    def degree(self):
    	print("Inside of getter")
    	return self.__degree
    	
    @degree.setter
    def degree(self, degree):
    	self._degree = degree
    	print("Inside of setter")
    	return self.__degree
    	
    	
man = Man('Bapon Kar', 'Teacher', 'M.Sc')

print(man.degree)
#print(man.name)
#print(man.profesion)





man.degree = 'M.Sc in Physics'
print(man.degree)

try:
    print(man.name)
except:
    print("Not printable")
