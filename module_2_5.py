def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        if m <= 0:
            break
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix
result1 = get_matrix(5, 3, 6)
result2 = get_matrix(0, 5, 6)
result3 = get_matrix(5, -25, 6)
print(result1)
print(result2)
print(result3)
