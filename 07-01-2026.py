# write a program for counting numbers

def Countdigi(n):
    cnt=0
    while n > 0:
        cnt = cnt +1
        n=n//10
    return cnt 

    if n ==0:
        print(1)

n = int(input())
print(Countdigi(n))