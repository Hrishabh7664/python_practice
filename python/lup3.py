#use trunc(), floor() and ceil() for numbers -2.8, -0.5, 0.2, 1.5 and 2.9 to
#  understand the difference between these functions clearly 
import math 
a = -2.8
b = -0.5
c = 0.2
d = 1.5
e = 2.9
print(math.trunc(a),math.floor(a),math.ceil(a))
print(math.trunc(c))
print(math.trunc(d))
print(math.trunc(e))
print(math.trunc(a))

# "EXPLANATION FROM MY SIDE"
# trunc works for rounding off values towards zero 

print(math.floor(a),math.floor(b),math.floor(c),math.floor(d),math.floor(e))
#floor rounds off towards negative infinity
#ceil must round off towards +ve infinity
print(math.ceil(a),math.ceil(b),math.ceil(c),math.ceil(d),math.ceil(e))


