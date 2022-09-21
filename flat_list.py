my_list = [[1], 10, 3, 2, 3, [1,2,3], [4,5], 8]

flat_list = []

for sub_list in my_list:
    if type(sub_list) != int:
        for num in sub_list:
            flat_list.append(num)
    else:
        flat_list.append(sub_list)

print(flat_list)