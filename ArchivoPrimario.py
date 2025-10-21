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


# def jumpingOnClouds(c):
#     # Write your code here
#     current = 0
#     jumps = 0
#     for place in range(len(c)):
#         try:
#             if (c[current+2]) == 0:
#                 current +=2
#                 jumps +=1
#             else:
#                 current +=1
#                 jumps+=1
#             if current >= len(c):
#                 break
#         except:
#             try:
#                 if (c[current+1]) == 0:
#                     current +=1
#                     jumps+=1
#             except:
#                 jumps = jumps
#     return jumps


# c= [0,0,1, 0, 0,1, 0]
# result = jumpingOnClouds(c)

# print(str(result) + '\n')

# def jumpingOnClouds(c):
#     current = 0
#     jumps = 0
#     while current < len(c) - 1:
#         if current + 2 < len(c) and c[current + 2] == 0:
#             current += 2
#         else:
#             current += 1
#         jumps += 1
#     return jumps