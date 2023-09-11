'''
Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. 
В результирующем списке не должно быть дубликатов.
'''
my_list = [3, 4, 3, 5, 6, 34, 45, 6]
print(my_list)

double_list = []

for i in my_list:
    if my_list.count(i) > 1:
        if i not in double_list:
            double_list.append(i)
print(double_list)