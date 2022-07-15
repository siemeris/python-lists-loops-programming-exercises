people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:
def deletePerson(person_name):
    #Your code go here:
    for element in people:
        if element == person_name:
            people.remove(person_name) 
    return people
    
print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))