def strcounter(s):
    s_count = {}
    for sym in s:
        s_count[sym] = s_count.get(sym, 0) + 1
    for sym, count in s_count.items():
        print(sym, count)
strcounter('abckfaa')