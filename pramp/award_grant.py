def find_grants_cap(grantsArray, newBudget):
  
  '''
  - least num of recipients impacted
  - new budget constraint is met (sum of N reallocated equals newBudget)
  [1,3,5,6,8], 11
         p
  '''
  
  # sort the array
  grantsArray.sort()
  
  # distribute from smallest to largest
  n = len(grantsArray)
  amt_left = float(newBudget)
  cap = 0
  
  for i in range(len(grantsArray)):
    try_give = amt_left / n
    if grantsArray[i] <= try_give:
      amt_left -= grantsArray[i]
    else:
      return amt_left / n
    
    n -= 1
  
  return cap