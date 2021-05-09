import unicodedata

name = unicodedata.name('A')
value = unicodedata.lookup(name)

print(name,value)


name1 = unicodedata.name('\u00a2')
value1 = unicodedata.lookup(name1)

print(name1,value1)


snowman = '\u2603'
value3 = unicodedata.lookup(snowman)
print(value3)
