colors = ["Red", "Green", "Pink", "Yellow"]

for color in colors:
    print(color)

print("last color:", color)

print("----------------------------")
for num in range(5):
    print(num)

print("----------------------------")
for num in range(1, 5):
    print(num)
    
print("----------------------------")
# += 2
for num in range(1, 7, 2):
    print(num)

print("----------------------------")
hex_colors = {"Red": "#212", "White": "#fff", "Black": "#000"}
for color in hex_colors:
    print(color)
for key, value in hex_colors.items():
    print(key, value)

# default value is 0
for index, value in enumerate(colors, 1):
    print(index, value)

print("----------------------------")
counter = 0
max = 4
while counter < max:
    print(counter)
    counter = counter + 1
    