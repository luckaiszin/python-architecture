from functools import reduce

# reduce applies a function cumulatively to the elements of an iterable and returns a single final value.

a = [5, 9, 3, 12, 7, 8, 5, 15, 28]

sum = reduce(lambda soma,atual: soma + atual, a)

print(sum)
