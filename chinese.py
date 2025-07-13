x=int(input())
days=[int(i) for i in input().split()]
nights=[int(i) for i in input().split()]
lim=int(input())



d=0
while(d<x):
    n=0
    while(n<x):
        if days[d]+nights[n]==lim:
            days.pop(d)
            nights.pop(n)
            x-=1
            continue
        n+=1
    d+=1
            
days.sort()
nights.sort(reverse=True) 
x=len(days)
i=0
pay=0
while(i<x):
    if days[i]+nights[i]>lim:
        pay+=days[i]+nights[i]-lim
    i+=1
print(pay*100)