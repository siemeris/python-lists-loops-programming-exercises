#Remember import random function here:
import random
my_list = [4,5,734,43,45]

#The magic is here:
for x in range(10):
    num = random.randint(0,1000)
    my_list.append(num)
    
print(my_list)
