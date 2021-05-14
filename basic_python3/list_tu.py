#List manipulation

my_list = [ "bapon", "bittu", "limbush", "tuktuki", 'jishu', 'Mathor']

print(my_list)

for i in my_list:
    print(i)

#firts_itm = my_list['bapon'] #showing error

first_itm = my_list[0]
print(first_itm)

print("new")
new = list("hello this is a list")
print(new)

new1 = "hello this is a list".split( ' ')
print(new1)

#Changing item by offset

new1[0] = "Hi"
print(new1)


#slice

new2 = new1[0:2]
print(new2)

new3 = new1[0:6:2]
print(new3)

new4 = new1[-2]
print(new4)

new5 = new1[0:2:-1]
print(new5)

new5.append("appending text")
print(new5)

#adding list
new6 = new1 + new5
print(new6)

new7 = new6 + new #adding new6 and new
print(new7)


#insert
print("new1:")
print(new1)
new8 = new1.insert(1,"inserted")#it's not working
print(new8)


del new1[0]
print(new1)

print("inserted" in new1)

sorted_new1 = sorted(new1)
print(sorted_new1)

length = len(new1)
print(length)

cnt = new.count("is")
print(new)


