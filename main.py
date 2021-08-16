from art import logo
print(logo)
def calculator():
 a=int(input("enter first number:"))
 b= input("enter operation +,-,*,/:")
 c = int(input("enter second number:"))

 if b== "+":
  print(f"the sum is {a+c}")
 elif b== "-":
  print(f"the substraction is {a-c}")
 elif b== "*":
  print(f"the multiplication is {a*c}")
 elif b== "/":
  print(f"the division is {a/c}")
  
calculator()
d= input("you want to continue operation yes or no:").lower
if d == "no":
  print("exit")
elif d== "yes":
   calculator()
  
  
  