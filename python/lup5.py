# write a program that generates 5 random numbers between 10 and 50.
# use a seed value of 6. make provision to change this seed value every time
# you execute the program by associating it with time of execution.

import random
import time


seed_value = 6 + int(time.time())
random.seed(seed_value)

for _ in range(5):
	print(random.randint(10, 50))


