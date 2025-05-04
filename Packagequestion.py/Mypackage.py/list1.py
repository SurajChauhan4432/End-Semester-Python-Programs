my_list = []

def append1(x):
    my_list.append(x)
    return my_list

def extend1(l):
    my_list.extend(l)
    return my_list

def pop():
    if my_list:
        return my_list.pop()
    return None

def remove1(x):
    if x in my_list:
        my_list.remove(x)
    return my_list
