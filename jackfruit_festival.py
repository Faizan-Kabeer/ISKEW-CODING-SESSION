n,d=[int(i) for i in input().split()]
arr=[int(i) for i in input().split()]

if n>d:
    arr.sort()
    print(sum(arr[n-1:n-d-1:-1]))
else:
    print(sum(arr))