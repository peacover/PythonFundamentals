def say_greeting(name, greeting="Hello"):
    # print(greeting, name)
    print(f"{greeting}, {name}")
    
    
# say_greeting("Youssef")
say_greeting("Youssef", "Bonjour")

names = ["test1", "test2", "test3"]
len_names = len(names)

numbers = [2, 33, 9, -2, 900, 10]
print(len_names)

sorted_nums = sorted(numbers)
sorted_nums_rev = sorted(numbers, reverse=True)
print(numbers, sorted_nums, sorted_nums_rev)
sorted_nums.sort()
print(sorted_nums)
sorted_nums.reverse()
print(sorted_nums)

vals = ["test1", "test2"]
added_vals = ["hello", "world"]
vals.extend(added_vals)
print(vals)

is_in = "test1" in vals
print(is_in)

test_names = ["test1", "test2", "test3", "test4", "test5"]
test_names.pop()
test_names.pop(1)
print(test_names)
test_names.remove("test1")
print(test_names)

test_names.insert(1, "added_val_insert")
test_names.append("added_val_append")
print(test_names)

my_list = ["H", "E", "L", "L", "O", "!"]
print(my_list[4:6])
print(my_list[:3])
print(my_list[-2:])
print(my_list[:-2])