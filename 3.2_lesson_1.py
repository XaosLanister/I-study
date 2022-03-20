d = {}


def update_dictionary(d, key, value):
    if key in d:
        d[key] += [value]
    else:
        key = 2 * key
        d.setdefault(key)
        d[key] = value
        d.update
        
update_dictionary(d, 1, -1)
print(d)