#Import random

#Create the function below:
def matrixBuilder(num):
    arr=[]
    lista=[]
    for item in range(0,num):
        arr.append(1)
    for item2 in range(0,num):
        lista.append(arr)
    return lista

print(matrixBuilder(5))
