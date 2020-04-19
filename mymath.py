# function is defined before you call it
def avg(list):
  sum = 0
  for e in list:
    sum = sum + e
  return sum/len(list)  