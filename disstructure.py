def calculate_structure_sum (data):
    global sum
    for i in data:
        if isinstance(i, str):
            sum += len(i)
        elif isinstance(i, int):
            sum += i
        elif isinstance(i, dict):
            calculate_structure_sum(i.keys())
            calculate_structure_sum(i.values())
        elif isinstance(i, (list, tuple, set)):
            calculate_structure_sum (i)

    return sum

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
sum = 0
print(calculate_structure_sum (data_structure))