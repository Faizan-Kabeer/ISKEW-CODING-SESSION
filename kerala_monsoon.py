n=int(input())
arr=[]
for i in range(n):
    arr.append([int(j) for j in input().split()])

stack=[]

for i in arr:
    if len(stack)>1:
        for j in range(len(stack)-1):
            if abs(stack[-1][0]-stack[j][0])<=stack[-1][1]-stack[j][1]:
                stack.pop(j)
    if stack:
        if abs(stack[-1][0]-i[0])>stack[-1][1]-i[1]:
            stack.append(i)
    else:
        stack.append(i)
if len(stack)>1:
        for j in range(len(stack)-1):
            if abs(stack[-1][0]-stack[j][0])<=stack[-1][1]-stack[j][1]:
                stack.pop(j)  
print(len(stack))

    