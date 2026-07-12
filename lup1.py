""" Q.  write a python program that swaps the values of variables 'a' and 'b'. you are not allowed to use third variable .yo
... u are not allowed to perform arithmetic on a and b """



# Initial values of the variables
a = 10
b = 20

print(f"Before swapping: a = {a}, b = {b}")

# Swapping without using a third variable or arithmetic operations
a, b = b, a

print(f"After swapping: a = {a}, b = {b}")