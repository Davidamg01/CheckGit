def sockMerchant(n, ar):
    count= 0
    allnumber = []
    for i in range(len(ar)):
        number = ar[i]
        if number not in allnumber:
            allnumber.append(number)
            HowMany = ar.count(number)
            count += int(HowMany/2)
    return count


n=9
ar= [10,20,20,10,10,30,50,10,20]
result = sockMerchant(n, ar)
print(str(result) + '\n')
