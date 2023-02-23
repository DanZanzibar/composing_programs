# Sequence unpacking: used with a sequence of sub-sequences, where the sub-sequences are a fixed length.

ex_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

new_list = []
for a, b, c in ex_list:
    new_list.append(a + b + c)


# List comprehension 

[sum(x) for x in ex_list if len(x) == 3]
generator = (sum(x) for x in ex_list if len(x) == 3)

def divisors(n):
    return [x for x in range(1, n) if n % x == 0]

def perfect_num(n):
    return [x for x in range(1, n) if x == sum(divisors(x))]

