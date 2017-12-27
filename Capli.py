a, b = map(int,input().split())
maximum = min(a, b)
m = max(a,b)
if m%2 == 1:
     print(m//2 +1, maximum)
else:
     print(m//2, maximum)
