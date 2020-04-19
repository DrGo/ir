# I want to create expense budget for my gas and utilites
# I want to know the total of individual spending and all 3 catergories per month

# Variables: gas,utilities
# I need to create the month (type, category?)
# Total expense- totalexp
# All expense - allexp

# I will need to create:
# loop to repeat per year
# convert to int
# creat strings
months= ["Jan", "Feb", "Mar"]
gas=[]
utils=[]
sums=[]
# open a file named expenses.txt; a+ when you want to add to existing file (not overwrite)
f = open("expenses.txt", "a+")
for month in months:
  print("what was your expenses for", month, "for each of the following:")
  g=float(input(" gas: "))
  # append= attach a value to the end of the list; starts with a dot
  gas.append(g)
  u=float(input(" utilities: "))
  utils.append(u)
  sum = g + u
  sums.append(sum)
  f.write(str(g)+ " "+ str(u) + " " + str(u))

for i in range(3):
  print("in", months[i], "you spent", sums[i])
  print("% on gas in ", months[i], gas[i]/sums[i]*100)
# print("gas", gas)
# print("utils", utils)
# print("sums", sums)
f.close()


  

#     if month==
#         print("Enter the total: ")
        
  
# myexp=["gas", "grocery", "utilities"]

# totalexp="y"
# allexp=0