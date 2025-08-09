#calculator
# we have 3 steps
#function for operation
#user input
#print result



def add(num1,num2):
     return num1+num2

def sub(num1,num2):
     return num1-num2

def multiply(num1,num2):
     return num1*num2

def divide(num1,num2):
     return num1/num2

def avg(num1,num2):
     return (num1+num2)/2


#useer input

print("please select a operation :\n "\
      "1. Addition\n"
      "2. subtract\n"
      "3. multiply\n"
      "4. divide\n"
      "5. average\n")

select = int(input("Select a operation from 1,2,3,4,5: "))
number1=int(input("enter first number:"))
number2=int(input("enter second number:"))


#step3 print result
if select==1:
   print(number1, "+",number2,"=",\
         add(number1,number2))

elif select==2:
   print(number1, "-",number2,"=",\
         sub(number1,number2))

elif select==3:
   print(number1, "*",number2,"=",\
         multiply(number1,number2))

elif select==4:
   print(number1, "/",number2,"=",\
         divide(number1,number2))

elif select==5:
  print("Average of", number1, "and", number2, "=",\
         avg(number1, number2))

else:
     print("invalid operation! pls select again!")