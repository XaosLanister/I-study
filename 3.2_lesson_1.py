d = {}


def update_dictionary(d, key, value):
    if key not in d:
        key = 2 * key
    if key in d:
        d[key] += [value]
    if key not in d:
        d.setdefault(key)
        d[key] = [value]
        d.update


update_dictionary(d, 1, -1)
update_dictionary(d, 2, -2)
update_dictionary(d, 1, -3)
print(d)