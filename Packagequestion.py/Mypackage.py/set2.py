my_set = set()

def slen2():
    return len(my_set)

def adds2(x):
    my_set.add(x)
    return my_set

def remove2(x):
    if x in my_set:
        my_set.remove(x)
    return my_set
