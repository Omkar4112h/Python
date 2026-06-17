print("Enter the two number for calculation")
num1 = int(input("Enter the 1st numbre: "))
opetaer = input("Enter the operatoer: ")
num2 = int(input("Enter the 2nd number: "))
op = "+,-,*,/"
if opetaer == "+":
    print(num1+num2)
elif opetaer == "-":
    print(num1-num2)
elif opetaer == "*":
    print(num1*num2)
else:
    print(num1/num2)


    