my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]

#your code go here:
new_list=[]
for element in my_list:
    if type(element)==dict or type(element)==list:
        new_list.append(element)

print(new_list)