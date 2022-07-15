list_of_numbers = [4,80,85,	59,	37, 25, 5, 64, 66, 81, 20, 64, 41, 22, 76, 76, 55, 96, 2, 68]


#Your code here:
def merge_two_list(list):
    evenList=[]
    oddList=[]
    for element in list:
        if element%2 ==0:
            evenList.append(element)
        elif element%2 !=0:
            oddList.append(element)
    return oddList + evenList

print(merge_two_list(list_of_numbers))

