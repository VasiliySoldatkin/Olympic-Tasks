a, b = map(int,input().split())
maximum = min(a, b)
if max(a,b)%2 == 1:
     print(max(a,b)//2 +1, maximum)
else:
     print(max(a,b)//2, maximum)
