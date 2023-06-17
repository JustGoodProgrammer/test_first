def pal(a):
    if a[::1] == a[::-1]:
        return True
    else:
        return False
    
s = input()
print(pal(s))