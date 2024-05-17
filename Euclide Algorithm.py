print(" enter two integers to find GCD Note: first number should be a>=b ")
num1=int(input("enter first number  "))
num2=int(input("enter second number "))
result=num1%num2
while result :
    num1=num2
    num2=result
    result=num1%num2
    print(num2)
print('Great Comman Divisior(GCD) is',num2)
