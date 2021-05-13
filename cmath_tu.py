import cmath

x = 4
y = 3

z = complex(x, y)

print(z)
print(z.real)
print(z.imag)

print(cmath.phase(z))

print(cmath.polar(z))

#Return the complex number x with polar coordinates r and phi. Equivalent to r * (math.cos(phi) + math.sin(phi)*1j).
print(cmath.rect(3,4))

