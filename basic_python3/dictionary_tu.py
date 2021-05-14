#dictionary manipulation



my_dict = { 'raju' : 'bapon', 'bittu' : 'bittu', 'limbush' : 'tanmoy','mathor' : 'sanjib'}

print(my_dict['bittu'])



#conversion
my_list = [['a','b'],['c','d'],['e','f']]
my_dict1 = dict(my_list)
print(my_dict1)

#changing value of a certain key
my_dict['raju'] = 'pushpendu'
print(my_dict)

#update
my_dict.update(my_dict1)
print(my_dict)


#deleting with a key

del my_dict[ 'a']
print(my_dict)

#deleting all item by clear

my_dict1.clear()

print(my_dict1)

#test a key

print('a' in my_dict)

#get all keys by key
print(my_dict.keys())

#get all values by value
print(my_dict.values())

#get all items by items i.e key-value pair
print(my_dict.items())



