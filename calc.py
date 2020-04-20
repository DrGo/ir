

x= int(input("enter first number: "))
y= int(input("enter second number: "))
op= input("enter * for multiplication, / for division, + for add")
if op=="*":
  result = x * y
elif op=="/":
  result = x / y
else:
  print("unknown operation")
print(result)
