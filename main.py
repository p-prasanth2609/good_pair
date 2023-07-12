a=list(map(int,input().split()))
b=int(input())
count=0
for i in range(len(a)):
    for j in range(len(a)):
        if i!=j:
            if(a[i]+a[j]==b):
                count+=1
count=count/2
print(int(count))
