books=[]
while 1==1:
    book =input("Please enter book name:")
    if book=="quit":
        break
    books.append(book)
print(books)
f = open("mybooks.txt", "a+")
for book in books:
    f.write(book + "\n")
f.close()
# def average(lst):
#     total=0
#     for n in lst:
#         total = total + n
#     avg = total / len(lst)    
#     return avg


# men=[1, 3, 5, 10, 17, 8, 21,30]
# women=[0, 2, 6, 10, 9, 8, 21,30]
# kids=[0, 2, 6, 10, 9, 8, 21,30]


# print("average for women:", average(women))
# print("average for men:", average(men))
# print("average for kids:", average(kids))

# # totalwomen=0
# # for n in women:
# #     totalwomen = totalwomen + n

# # print("total men", totalmen)
# # print("total women", totalwomen)
# # print("total cases", totalmen + totalwomen)
# # numday= len(men)
# # print("avertage men", totalmen / numday)
# # print("avertage women", totalwomen/ numday)
# # print("avertage cases", (totalmen + totalwomen) / numday)

# for i in range(1,10):
#     print(i)