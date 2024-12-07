immutable_var = 1, 5, True, 'point'
print(immutable_var)
#immutable_var[0] = 3 #кортеж неизменяем, поэтому появляется ошибка
mutable_list = [3, 7, 'a pig']
mutable_list[2] = 'a goat'
print(mutable_list)