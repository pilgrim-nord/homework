n = int(input())
list_ = []
for i in range(1, n + 1):
    for j in range(1, n  + 1):
        if n % (i + j) == 0 and i < j:
            list_.append(i)
            list_.append(j)
print (*list_, sep='')
