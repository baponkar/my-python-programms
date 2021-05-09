import re

source = 'Young Frankeinstein'

m = re.sub("n", "$",source)
print(m)
#print(m.group())
