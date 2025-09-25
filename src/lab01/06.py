n = int(input())
countt = 0  
countf = 0   
for _ in range(n):
    dan = input().split()
    if dan[3] == "True":
        countt += 1
    else:
        countf += 1
print(countt, countf)