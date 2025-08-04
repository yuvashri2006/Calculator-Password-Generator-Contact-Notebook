num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
while True:
    choice=input("Operation Choice(1.Addition,2.Subtraction,3.Multiplication,4.Division):")
    if choice=="1":
        print("Result:",num1+num2)
        break
    elif choice =="2":
        print("Result:",num1-num2)
        break
    elif choice=="3":
       print("Result:",num1*num2)
       break
