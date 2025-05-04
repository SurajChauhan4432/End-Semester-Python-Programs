import list1
import set2
import dict3

# Using list1 module
print("List Operations:")
print("Append 10:", list1.append1(10))
print("Extend [20, 30]:", list1.extend1([20, 30]))
print("Remove 20:", list1.remove1(20))
print("Pop:", list1.pop())

# Using set2 module
print("\nSet Operations:")
print("Add 'apple':", set2.adds2("apple"))
print("Add 'banana':", set2.adds2("banana"))
print("Remove 'apple':", set2.remove2("apple"))
print("Set Length:", set2.slen2())

# Using dict3 module
print("\nDictionary Operations:")
print("Add key-value (name, John):", dict3.add3("name", "John"))
print("Add key-value (age, 25):", dict3.add3("age", 25))
print("Keys:", dict3.keys3())
print("Values:", dict3.values3())
print("Dictionary Length:", dict3.len3())
