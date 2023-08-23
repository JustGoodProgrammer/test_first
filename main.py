for i in range(int(input())):
    a = int(input())
    b = bin(a-1)[2:]
    if '111' in b:
        b = b[b.rfind('1')-2:]
        print(int(b, base=2))
    else:
        print(-1)
