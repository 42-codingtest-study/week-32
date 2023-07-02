# 15강 _ 회사에 있는 사람
# 시간 초과 pypy로 제출

n = int(input())
dic = {}

for _ in range(n):
    name, log = input().split()
    dic[name] = log
    if log == "leave":
        del dic[name]

d = sorted(dic.items(), reverse = True)
dic = dict(d)

for key in dic.keys():
    print(key)