# def sockMerchant(n, ar):
#     count= 0
#     allnumber = []
#     for i in range(len(ar)):
#         number = ar[i]
#         if number not in allnumber:
#             allnumber.append(number)
#             HowMany = ar.count(number)
#             count += int(HowMany/2)
#     return count


# n=9
# ar= [10,20,20,10,10,30,50,10,20]
# result = sockMerchant(n, ar)
# print(str(result) + '\n')


# def countingValleys(steps, path):
#     count= 0
#     valley=0
#     for step in range(len(path)):
#         current = path[step]
#         if current == "U":
#             count +=1
#             if count == 0:
#                 path[step-1] == "D"
#                 valley +=1
#         else:
#             count-=1

#     return valley


# steps = 12
# path = ["D","D","U","U","D","D","U","D","U","U","U","D"]
# result = countingValleys(steps, path)

# print(str(result) + '\n')


#            /\
# \   /\    /
#  \ /  \/\/