def root(x, n):
  
  l, r = 0, max(1, x)
  
  while (r - l) >= 0.001:
    m = (l + r) / 2.0

    if m ** n == x:
      return m
    
    if m ** n > x:
      r = m
    else:
      l = m
      
  return m 