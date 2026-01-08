# Second Largest Element in an Array without sorting

gnum=0
gnum2=0
arr=list(map(int,input().split(',')))
ar2=[]

for i in arr:
    if i>gnum:
        gnum=i

for i in arr:
    if i!=gnum:
        ar2.append(i)

for i in ar2:
    if i>gnum2:
        gnum2=i


print(gnum2)