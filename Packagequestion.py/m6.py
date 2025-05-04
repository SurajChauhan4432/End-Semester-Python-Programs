from mypackage import append1, extend1, pop, remove1
from mypackage import adds2, remove2, slen2
from mypackage import add3, keys3, values3, len3

# List operations
print("List append:", append1(100))
print("List extend:", extend1([200, 300]))
print("List remove:", remove1(200))
print("List pop:", pop())

# Set operations
print("Set add:", adds2("banana"))
print("Set remove:", remove2("banana"))
print("Set length:", slen2())

# Dictionary operations
print("Dict add:", add3("name", "Alice"))
print("Dict keys:", keys3())
print("Dict values:", values3())
print("Dict length:", len3())
