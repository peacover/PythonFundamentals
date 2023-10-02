my_str = "this,is,a,test"

my_str1 = my_str.split(",")
print(my_str1)

my_str2 = ": ".join(my_str1)
print(my_str2)

# remove first and last spaces
my_str = "    |this is       a test|   "
print(my_str.strip())
print(my_str.lstrip())
print(my_str.rstrip())

x = 2e8
y = 3e10
z = x + y
print(f"{z:,} | {int(z):,}")
# another annotation of round
x = 2.675
y = 3.123
z = x + y
print(f"{z:.2f} | {round(z, 2)}")

# to string
num = 14
to_str = str(50)
print(to_str, type(to_str))

greeting = "hello"
to_list = list(greeting)
print(to_list)

print("----------------------------")
names = ["Youssef", "Max", "Akali", "Graves"]

to_upper_names = []
for name in names:
    to_upper_names.append(name.upper())
print(to_upper_names)

print ([name.upper() for name in names])

print("----------------------------")
print(list(range(4)))
print([num * num for num in range(6)])

print("----------------------------")
print([("lenght", len(name)) for name in names])

print("----------------------------")
print(" ,".join([f"My name is {name}" for name in names]))

print("----------------------------")
even_squares = [num * num for num in range(6) if num % 2 == 0]
print(even_squares)
combined_result = ", ".join([str(num) for num in even_squares])
print(combined_result)

print("----------------------------")
lottery_num_string = "123, 8, 33, 222, 45"
max_num = max([int(l_str) for l_str in lottery_num_string.split(", ")])
print(max_num)

print("----------------------------")
print({num: num * num for num in range(6)})

# generator exp 
print("----------------------------")
res = max(num for num in range(6))
print(res)

print("----------------------------")
# my_list = list(range(10))
my_list = [2,3,55,77,9,100,87,44,5550]
print(my_list)
print(my_list[::2])
print(my_list[::3])
# [start:len:step]
print(my_list[1:7:2])
# reverse with step
print(my_list[::-1])
print(my_list[::-2])

# zip function : create a tuple from two lists 
print("----------------------------")
players = ["Evelynn", "Graves", "Jarvan"]
scores = [65, 55, 78]
res_zip = zip(scores, players)
for item in res_zip:
    print(item)
print([f"score : {score} | player : {player}" for score, player in zip(scores, players)])
to_dict = dict(zip(players, scores))
print(to_dict)
to_list = list(zip(players, scores))
print(to_list)

print("----------------------------")

import random
tmp_str = ["test1", "test2", "test3", "test4", "test5"]
# copy list
# test = tmp_str.copy()
test = tmp_str[:]
random.shuffle(test)
print(tmp_str)
print(test)
for item in sorted(test):
    print(item)
print("----------------------------")

for item in sorted(test, reverse=True):
    print(item)
print("----------------------------")

for item in reversed(test):
    print(item)
print("----------------------------")
print(test)
# sorted(test) create a new list
# test.sort() modify the list

print("----------------------------")

students = [{"name": "Student1", "score": 90}, {"name": "Student2", "score": 40}, {"name": "Student3", "score": 70}]

def get_score(student):
    return student["score"]

for student in sorted(students, key=get_score):
    print(student)
print("----------------------------")
for student in sorted(students, key=lambda item: item["score"]):
    print(student)