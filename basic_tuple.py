# tuple are immutable (we cant add or remove from it)

# creation: () or tuple() or (1, ) for one item
student = ("Youssef", 16, "History", 4.3)
print(student)

name, age, subject, gpa = student
print(name, age, subject, gpa);

#also this is a tupe cz of the COMMAS!
x = 1, 2, 3
print(type(x))

def http_status_code():
    return 200, "OK"
code, name = http_status_code()
print(code)
print(name)

founded_val_index = student.index(16)
print(founded_val_index)
