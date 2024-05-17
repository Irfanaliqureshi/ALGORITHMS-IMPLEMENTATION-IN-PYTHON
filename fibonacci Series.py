def fibnacci(n):
  if n==0:
    return 0 
  elif n==1:
    return 1
  else:
    return fibnacci(n-1)+fibnacci(n-2)
for i in range(10):
  print(fibnacci(i))
