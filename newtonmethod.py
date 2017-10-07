import decimal

print("We are finding the square root of an integer using Newton's Method")
q = raw_input("Which number should we find the square root of? ")
r=int(q)

x = raw_input('What is the first guess?')
x = int(x)

def polynomial(x):
    return x**2-r
   

def deriv(x):
    return 2*x



p=0
y = polynomial(p)
z=1

while z > .001:
    x = float(x) - (float(polynomial(x))/float(deriv(x)))
    z = (polynomial(x))
    print(z)
    print(x)