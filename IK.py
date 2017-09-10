import math





# returns the length of link 2 through the given coordinates
def solveL22(x, y):
    a = 1
    b = -2 * x
    c = x**2 - y **2


    print('a: ' + str(a))
    print('b: ' + str(b))
    print('c: ' + str(c))    


    return (-b + (b**2 - (4 * a * c))**0.5)/(2 * a)

# returns the length of link 1 through x-coordinate
def solveL11(x):
    return x/math.cos(math.radians(45))

def solveL222(x, y):
    a = 1
    b = -2 * x
    c = x**2 - y **2


    print('a: ' + str(a))
    print('b: ' + str(b))
    print('c: ' + str(c))    


    return (-b + (b**2 - (4 * a * c))**0.5)/(2 * a)