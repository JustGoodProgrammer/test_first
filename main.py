'''for i in range(int(input())):
    a = int(input())
    b = bin(a-1)[2:]
    if '111' in b:
        b = b[b.rfind('1')-2:]
        print(int(b, base=2))
    else:
        print(-1)'''
a = int(input())
l = [int(i) for i in input().split()]
ans = []

if a % 2 == 0:
    print('no')
else:
    for i in range(a//2):
        b = max(l)
        ans.append(b)
        l.remove(b)
    if ans[-1] > max(l):
        print('yes')
    else:
        print('no')
