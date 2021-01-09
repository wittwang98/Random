print("Input number of points to approximate Pi\n")

points = int(input())

import random
inside = 0
percentage = 0

for a in range(points):
    b = (random.random(), random.random())
    if (b[0]**2 + b[1]**2)**(0.5) <= 1:
        inside += 1
    if a%(points/100) == False:
        percentage += 1
        print(percentage, "%")
    
print("Pi is approximatively ", (4.0*inside/points))