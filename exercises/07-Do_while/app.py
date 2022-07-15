
#Your code go here:

x=21
while x>=1:
    x-=1 
    if x==0:
        print("LIFTOFF")
    elif x%5 == 0:
        print(str(x) + "!")

    else:
        print(x)