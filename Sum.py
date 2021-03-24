import sys
N = int(sys.stdin.readline())
result = 0
if N<=0:
    N*=(-1)
    result = N*(N+1) // 2
    result = -result + 1
    print(result)
else:
    result = N*(N+1) // 2
    print(result)
