#page - 106

guess_me = 7

if guess_me < 7:
    print("Too low")
elif guess_me == 7:
    print("That's right")
else:
    print("Too high")


even_numbers = []
for i in range(10):
    if i % 2 == 0:
        even_numbers.append(i)

print(even_numbers)




square_dict = {}

for i in range(10):
    sqr = i ** 2
    square_dict[str(i)] = str(sqr)

print(square_dict)




odd_set = {}
odd_set = {val for val in range(10) if val % 2 != 0 }

print(odd_set)


def dec(func):
    def new_func(*args,**kwargs):
        print("Start")
        result = func(*args,**kwargs)
        #result = 10
        print("End")
        return result
    return new_func

@dec
def add(x,y):
    res = x + y
    print(res)
    return res

add(19,45)

