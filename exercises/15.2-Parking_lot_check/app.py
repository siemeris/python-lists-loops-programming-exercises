parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

#Your code go here:
def get_parking_lot(obj): 
  state={}

  available_slots=0
  occupied_slots=0
  total_slots=0

  for item in obj:
    for element in item:
      if element==2:
        available_slots +=1
        total_slots +=1
      elif element ==1:
        occupied_slots +=1
        total_slots +=1

  state["total_slots"]=total_slots
  state["available_slots"]=available_slots
  state["occupied_slots"]=occupied_slots

  return state

print(get_parking_lot(parking_state))







