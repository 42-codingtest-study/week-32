# 14강 _ 수 고르기

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

arr.sort()
left, right = 0, 0
res = 2000000000

while left < n and right < n :
    if arr[right] - arr[left] < m :
        right += 1
    else :
        res = min(res, arr[right] - arr[left])
        left += 1

print(res)