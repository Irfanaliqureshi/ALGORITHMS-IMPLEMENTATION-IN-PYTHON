num=int(input("Enter a number for Factorial  "))
factorial=1
if num<0 | num==0:
  print("Sorry factorial does not exist")
else:
    for i in range(1,num+1):
       factorial=factorial*i
       print(factorial) 
