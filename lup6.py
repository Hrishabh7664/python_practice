#given three sides a,b,c of a triangle , write program to obtain and print the values of three angles rounded
# to the next integer
import math

a = 3
b = 4
c = 5

x = (pow(b,2) + pow(c,2) - pow(a,2)) / (2*b*c)
y = (pow(b,2)+pow(a,2)-pow(c,2))/(2*b*a)
z = (pow(c,2)+pow(a,2)-pow(b,2))/(2*c*a)


print(math.ceil(math.degrees(math.acos(x))))
print(math.ceil(math.degrees(math.acos(y))))
print(math.ceil(math.degrees(math.acos(z))))      

