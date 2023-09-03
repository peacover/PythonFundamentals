# creation: set() ex: {1} 
# set object doesnt support indexing!!! we cant do names[0]
# set doesnt keep the order!
# very fast when searching for item 

names = {"Youssef", "Max", "Youssef"}
print(names, type(names))

list_names = ["Youssef", "Max", "Youssef"]
set_names = set(names)
print(set_names)

colors = {"Red", "Green", "Pink"}
colors.add("Blue")
print(colors)
colors.discard("Red")
print(colors)
# remove throw error when it's not fount!!
colors.remove("Blue")
print(colors)


numbers = {2, 3, 1}
colors.update(numbers)
print(colors)
# !!!
colors.update("TEST")
print(colors)

# check if exist 
print("Pink" in colors)

# union
# union : my_set.union(other_set) or my_set | other_set
all_colors = {"Blue", "Red", "Black", "Pink", "Yellow", "Green"}
fav_colors = {"white", "Orange", "Blue"}

# res_union = all_colors.union(fav_colors)
res_union = all_colors | fav_colors
print(res_union)


#intersection
# res_inter = all_colors.intersection(fav_colors)
res_inter = all_colors & fav_colors
print(res_inter)

#the difference
# res_difference = all_colors.difference(fav_colors)
res_difference = all_colors ^ fav_colors
print(res_difference)