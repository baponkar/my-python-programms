class Duck():
    def __init__(self, input_name):
        self.__name = input_name
   
        


        @property
        def name(self ):
            print("Inside the getter!")
            print(self.__name)
            return self.__name

        @name.setter
        def name(self, input_name):
            print("inside the setter!")
            self.__name = input_name


fowl = Duck("Howard") 


print(fowl.name)

fowl.Name = 'Donald'
print(fowl.Name)

