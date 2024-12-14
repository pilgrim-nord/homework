# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# primes, not_primes = [], []
# for i in numbers:
#     if i == 1:
#         not_primes.append(i)
#         continue
#     for j in numbers[1 :]:
#         if i % j != 0:
#             continue
#         if i % j == 0 and i == j:
#             primes.append(i)
#             break
#         else:
#             if i % j == 0 and i != j:
#                 not_primes.append(i)
#             break
#
#
# print('Primes:', primes)
# print('Not primes:', not_primes)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for num in numbers:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)
    else:
        not_primes.append(num)
print('Primes:', primes)
print('Not primes:', not_primes)