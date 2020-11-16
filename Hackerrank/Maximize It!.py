"""
Problem
https://www.hackerrank.com/challenges/maximize-it/problem
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
K, M = list(map(int, input().split()))
n_lists = []
max_list = 0
for i in range(K):
    # Set to make it unique as you can only pick one
    # The first element in the list is the number of items in the list
    n_lists.append(list(set(map(int, input().split()[1:]))))

permutations = list(itertools.product(*n_lists))

max_modulus = 0
for permutation in permutations:
    total = 0
    for item in permutation:
        total += item ** 2
    max_modulus = max(max_modulus, total % M)
print(max_modulus)
