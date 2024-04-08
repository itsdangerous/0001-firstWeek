from itertools import combinations_with_replacement

N, M = map(int, input().split())
arr = list(map(int, input().split()))
res = sorted(list(set(combinations_with_replacement(arr, M))))

for i in res:
    for j in i:
        print(j, end=" ")
    print()
