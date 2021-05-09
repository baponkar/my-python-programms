#set manipulation

#SET means value less dictionary


my_set = { 0,1,2,3,4,5,6,7,8,9}
odd_set = {1,3,5,7,9}
even_set = {2,4,6,8}

print(my_set)
#print(my_set[5]) #This will not works in case of set

for i in my_set:
    print(i)


#string to set

my_set1 = set('letters')

print(my_set1) #one alphabet only once occurs

#set operations

#intersection
ints = my_set.intersection(odd_set)
print(ints)

#Union
uni = odd_set | even_set
print(uni)

#difference
diff = my_set.difference(even_set) #alternative my_set - even_set
print(diff)


#subset
print(odd_set.issubset(my_set)) #alternative odd_set <= my_set

#superset
print(my_set.issuperset(odd_set)) #alternative my_set >= odd_set

#proper subset
print(even_set < my_set)

#proper superset
print(my_set > even_set)


#exercises
years_list = [ 1987,1988,1989,1990,1991]

print("My third birthday : " + str(years_list[4]))

things = [ 'mozzarella', 'cinderella', 'salmonella' ]

#print(things.capitalize())
j = 0
for i in things:
    print(i.capitalize())
    things[j] = i.capitalize()
    j = j + 1

things = things + ['disease','chessy'.upper()]

things.remove('disease')
print(things)

surprise = [ 'Groucho', 'Chico', 'Harpo' ]
print(surprise[2].lower()[::-1].capitalize())

#english to frencch dictionary

e2f = { 'dog' : 'chien','cat' : 'chat', 'walrus' : 'morse' }
print(e2f)
print(e2f['walrus'])

f2e = dict({})
for i,j in e2f.items():
    f2e[j] = i

print(f2e)


life = {'animals' : {'cats' : ['Henri','Grumpy', 'Lucy'], 'octopi' : {},  'emus' : {} }, 'plants' : {}, 'other' : {} }

print(type(life.keys()))

print(life['animals'].keys())

print(life['animals']['cats'])
