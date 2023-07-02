# 14강 _ 회전 초밥
# 시간 초과로 pypy로 제출함

import sys

n, d, k, c = map(int, sys.stdin.readline().rsplit())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
left, right = 0, 0
ans = 0

while left != n :
    right = left + k
    case = set()
    add = True
    for i in range(left, right) :
        i %= n
        case.add(arr[i])
        if arr[i] == c :
            add = False

    cnt = len(case)
    if add:
        cnt += 1
    ans = max(ans, cnt)
    left += 1

print(ans)