my_list = [43,23,6,87,43,1,4,6,3,67,8,3445,3,7,5435,63,346,3,456,734,6,34]

#Your code go from here:
def Max(lista):
    aux = 0
    for item in lista:
        if item>aux:
            aux=item
    return aux

print(Max(my_list))
