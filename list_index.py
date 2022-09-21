from multiprocessing.sharedctypes import Value


my_list = [2, 6, 8, 10, 13]

for id in range(len(my_list)):
    value = my_list[id]
    print(id, value)
