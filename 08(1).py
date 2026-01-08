# Find the Largest element in an array

gnum=0
arr=list(map(int,input().split(',')))
for i in arr:
    if i>gnum:
        gnum=i

print(gnum)