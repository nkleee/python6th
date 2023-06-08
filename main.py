fruits = ["apple", "banana", "cherry", "orange"]

print(fruits)

fruits.append("grape")

print(fruits)

fruits.insert(2, "kiwi")

print(fruits)

print(fruits.pop())
print(fruits.pop(1))

print(fruits)

fruits.append("cherry")
print(fruits)

print(fruits.index("cherry"))
print(fruits.remove("cherry")) #remove는 중복된 값이 있다면 하나만 지운다
print(fruits.index("cherry"))
print(fruits.remove("cherry"))
# print(fruits.index("cherry"))

fruits.reverse()

print(fruits)