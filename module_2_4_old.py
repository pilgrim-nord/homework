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
