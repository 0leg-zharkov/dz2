my_list = [1, -2, False, 3.4, "Help", [1, 2, 3]]
p = dict()

for n in range(len(my_list)):
    p[n] = type(my_list[n])

print(p)
