
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list[1:4])
print(my_list[2])

my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list_1 = list(set(my_list))
print(unique_list_1)

unique_list_2 = []

for i in my_list:
    if i not in unique_list_2:
        unique_list_2.append(i)

print(unique_list_2) 

my_list = [10, 20, 4, 45, 99]
print(my_list)
my_list.sort()
print(my_list)
print(my_list[-2])