responses = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 2]
# for i in range(1,6):
#     print(f'{i:>4} appears  {responses.count(i)}')


# for unknown range

unique_num = sorted(set(responses))
for i in unique_num:
   print(f'{i:>4} appears  {unique_num.count(i)}')