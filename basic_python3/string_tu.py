# The string manipulation

alphabet = "abcdefghijklmnopqrstuvwxyz"
print(len(alphabet))
#alphabet[start:end:step]
print(alphabet[0:25:3])

print(alphabet[1::])

print(alphabet[:10:])

print(alphabet[::3])

print(alphabet[-5::]) #printing the five from last to first
print(alphabet[:-5:]) #printing from first to fifth position from last

print(alphabet[::-3]) #from last to first with 3 step

print(alphabet.split('k'))

split_string = alphabet.split('k')

join_string = ",".join(split_string)

print(join_string)

#keep mind that counting from left side alaways start from 0 but counting from right alaways start from -1
print(alphabet[5]) #f

print(alphabet[-25]) #b

print(alphabet.upper())

print(alphabet.swapcase()) #swaping between upper and lower case

print(alphabet.title()) # the first alphabet of each different word get capitalize

print(alphabet.capitalize) #first word's first alphabet get capital

print(alphabet.center(30))
print(alphabet.ljust(30))
print(alphabet.rjust(30))


my_string = "This is my string"
your_string = my_string.replace('my','your')
print(your_string)


#exercise Page-39

hour = int(input("Enter the time in hour : "))

seconds = hour * 3600
print(seconds)






