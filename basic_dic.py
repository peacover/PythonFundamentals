dic1 = {1: 'test', 3:'test3'}

# return when not exist: dic1[2]
# return nothing when not exist: dic1.get(2)
print(dic1[1], dic1.get(1))
print(dic1.get(2, "default value"))

colors = {"r": "Red", "g": "Green"}
numbers = {"1": "One", "2": "Two", "r": "TEST"}
colors.update(numbers)
colors["added_key"] = "added_value"
print(colors)

print(colors.keys())
print(colors.values())
print(colors.items())

