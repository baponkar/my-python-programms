#tupules are immutable i.e. not changeble

my_tuple = ('raju', 'bittu', 'bapon', 'babai', 'mathor', 'bijoy')

print(my_tuple)

print(my_tuple[0])

#my_tuple[0] = 'sanjib' #not works

print(my_tuple)

my_tuple1 = ( 'mou', 'anuska' )
my_tuple2 = my_tuple + my_tuple1

print(my_tuple2)

print(len(my_tuple))


for i in my_tuple:
    print(i+"==>")
