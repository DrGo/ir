# ask the user for number between 1 and 10
# store number in a variable of type (int)
import random
secret= random.randrange(10)
num= 0
trial=3
while trial > 0:
  num=int(input("Pls select number between 1 and 10: "))
  trial = trial-1
  print("you have this many trials left:", trial)
# compare number with 5
# if number is equal to 5 type "you won!"
# if number if more than 5 type "too high!"
# if number if less than 5 type "too low!"
  if num==secret:
    print("you won!")
    break    
  elif num>secret:
    print("too high!")
  else:
    print("too low") 
if trial <0:     
  print("you lost")


