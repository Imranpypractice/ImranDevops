#name = input("what is your name?:")
#print(f"hello {name}")
# returning multiple values from a function
 
def circle(r):
    area = 3.14*r*r
    circumfurence = 2*3.14*r
    return area,circumfurence
 
# calling the function and extracting ghe value
a,c = circle(10)
print(f"Area of a circle is {a}, circumference is {c}")