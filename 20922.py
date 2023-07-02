# 14강 _ 겹치는 건 싫어

import sys

input = sys.stdin.readline
n, k = map(int,input().rstrip().split())
len = list(map(int,input().rstrip().split()))

ans = 0
dic = {}
left, right = 0, 0

while right < n :
    r_cnt = dic.get(len[right],0)
    if r_cnt < k :
        dic[len[right]] = dic.get(len[right], 0) + 1
        right += 1
    else :
        dic[len[left]] = dic.get(len[left], 0) - 1
        left += 1
    ans = max(ans, right - left)

print(ans)