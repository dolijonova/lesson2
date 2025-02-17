print("Task 1")
username=input("Please enter your username")
password=input("Please enter your password")
if username.strip()=="" and password.strip()=="":
    print("Password and username cannot be empty.")
else:
    print("Your password and username is correct")
print("Task 2")
number1=int(input("Enter an integer number"))
number2=int(input("Enter an integer number"))
def checkequality(num1,num2):
    if num1==num2:
        return True
    else:
        return False
equality=checkequality(number1,number2)
print(equality)
print("Task 3")
def positiveandeven(num):
    if num>0 and num%2==0:
        return True
    else:
        return False
number3=int(input("Input a number"))
if positiveandeven(number3)==True:
    print("NUmber is positive and even")
else:
    print("The number is not positive or even")
print("Task 4")
numb1=int(input("Enter a number"))
numb2=int(input("Enter 2nd number"))
numb3=int(input("Enter your 3 rd number"))
if numb1!=numb2 and numb2!=numb3 and numb1!=numb3:
    print("The number are not equal")
else:
    print("The numbers may be equal")
print("Task 5")
string1=input()
string2=input()
if len(string1)==len(string2):
    print("They have the same length")
else:
    print("They are not the same length")
print("Task 6")
number=int(input())
if number%3==0 and number%5==0:
    print("Number is divisible by both 3 and 5")
else:
    print("Number is not divisible by both 3 and 5")
print("Task 7")
number11=int(input("Enter a number"))
number22=int(input("ENter another number"))
if number11+number22>50:
    print("The sum of your first and second number is greater than 50")
else:
    print("The sum of your numbers are not greater than 50")
print("Task 8")
number33=int(input("Enter the last number"))
if number33<=20 and number33>=10:
    print(" The number is between 20 and 10")
else: 
    print("The number is not between 10 and 20")