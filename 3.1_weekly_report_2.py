def modify_list(lst):
    i, n = 0, len(lst)
    while i < n:
        if lst[i] % 2:
            lst.pop(i)
            n -= 1
        else:
            lst[i] = lst[i] // 2
            i += 1