def find_grants_cap(grantsArray, newBudget):
  grantsArray.sort()
  n = len(grantsArray)
  remaining = newBudget
  
  for grant in grantsArray:
    evenly_divided = remaining / n
    
    if grant <= evenly_divided:
      remaining -= grant
    else:
      return evenly_divided
    
    n -= 1
  
  return evenly_divided

grantsArray = [2, 4]
newBudget = 3
print(find_grants_cap(grantsArray, newBudget))