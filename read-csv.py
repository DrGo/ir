
def readAll():
  f = open("students.csv", "r")
  content= f.readlines()
  # print(content)
  for line in content:
    # print(line)
    words = line.split(", ")
    for word in words:
       print('{:^12}'.format(word), end='')
    print("")     
  f.close()

def addStudent():
  f = open("students.csv", "a")
  name=input("Enter student name: ")
  age=int(input("Enter student age: "))
  degree=input("Enter student degree: ")
  f.write(name + ", " + str(age) + ", " + degree + "\n")
  f.close()

# make a menu
print("Student management program")
print("press 1 to see all student data")
print("press 2 to add a student data")
print("press 3 to exit")
choice=int(input("make a choice: "))
if choice==1:
  readAll()
elif choice==2:  
  addStudent()  
else:
  print("good bye")  