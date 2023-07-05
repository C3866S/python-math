# CRC (cyclic redundancy check)

#Use case: Ethnernet protocol or data compression in the form of ZIP archives or images in the PNG format
#I will only work with Z2[x]
#Attention; all bit sequences represented here are polynoms and not binary numbers!

#Define g, the "Generator Polynom" i.e.

#g = 110101  x⁵+x⁴+x²+1

#Send the data [the bit string] "called frame"
#In this example we will set p as:

#p = 11011  this polynom will be multiplied with x^n, where n = g  this means; n = g = x⁵

#this results in 1101100000 [the last 0 are the x⁵ from g]

# Now the polynom will be divided by g, but we are only interested in the remainder

from sympy import *

x = symbols("x")

g = Poly(x**5+x**4+x**2+1)

p = Poly(x**4+x**3+x+1)

r = rem(p, g)

r

#replace the 0 of p with r; r=101 => m = 1101100101

m = p + r
m

#why? primarily because I hate myself, but in Z2 a subtraction equals the addition this means

#                                      m=p+r  ==  m=p-r

#This also means m:g=0, therefore g has to be a divider of m
#That's it! The receiver of the bit string m divides g, if g is not 0 then you have a so called "transmission error"

rem(m, g)                               #Ok,remainder is 0
rem(m + Poly(x**8, modulus=2), g)       #second bit error

#Even with an error, it is still possible to get a 0
rem(m + Poly(x**8+x**7+x**6+x, modulus=2), g)       # 4 bits are incorrect

#the hardest part is to have a g whose remainder does not extinguish by the number of errors

#We can also say it like that: the polynom m got send, but the received polynom is mF (with potential flaws/errors)
# this holds true to mF= m+e
#whereas e is a bit sequence where the 1's are on a spot with errors, therefore the letter e for "error polynom"
#after construction, it applies to g|e avoid g|mF at all cost this means: no g|e [because with m and e their sum mF would also be divisble by g]


#If you have a lot of time run this:

def divides (q, p):
    return rem (p, q).is_zero

q = Poly(x**15 + x**14 + 1, modulus=2)
k = 1

while not divides(q, Poly(x**k + 1, modulus=2)):
    k += 1
k

#The polynom x¹⁵+x¹⁴+1 has a nice feature, till k=32767 there is not a single polynom, in the form of x^k+1, to divide


























