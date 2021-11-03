def first(lst):
    d = {}
    while(len(lst) > 0):
        key = lst.pop(-1)
        item = lst.count(key)
        d[key] = item + 1
    
    return sum([d[item] for item in d])

lst = [1, 2, 3, 1, 2, 3]
print(first(lst))