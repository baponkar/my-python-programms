import re

source = 'Young Frankenstein'

m = re.match('You', source)
print(m)

if m:
    print(m.group())


m1 = re.match('^You', source)
if m1:
    print(m1.group())


m2 = re.match('.*in$',source)
if m2:
    print(m2.group())

print("-----")
m3 = re.match('Frank',source)
if m3:
    print(m3.group())




