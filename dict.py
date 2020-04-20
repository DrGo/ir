# create a dict
# lang={"hi": "hola", "my": "mi", "I" : "Yo"}
# use as a list but enter the value of the left word
# print(lang["I"])
# print(lang["Ok"])
lang={}

def getKeyValue():
  # print("inside getKeyValue")
  key = input("Enter key: ")
  value = input("Enter value:")
  lang[key]=value
  # print("leaving getKeyValue")

getKeyValue()
# getKeyValue()
# getKeyValue()

print(lang)

