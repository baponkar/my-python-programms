class testDec(object):                                                                                                                                            

    def __init__(self, value):
        print( 'We are in __init__')
        self._x = value # Will call the setter. Note just x here
        #self._x = value # Will not call the setter

    @property
    def x(self):
        print ('called getter')
        return self._x # Note the _x here

    @x.setter
    def x(self, value): 
        print ('called setter')
        self._x = value # Note the _x here

t = testDec(17)
print (t.x )
