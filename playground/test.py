list_a = [1, 2, 3]
list_b = []

for item in list_a:
    list_b.append(item)

print(list_b)

list_a.pop()
print("list_a po pop: ", list_a)
print("list_b: ", list_b)
