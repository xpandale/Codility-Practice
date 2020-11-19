#https://www.hackerrank.com/challenges/validating-credit-card-number/problem
import re
n = int(input())
for i in range(n):
    _input = input()
    out = "Valid" if re.search(r"^[4-6]{1}\d{3}(-|)\d{4}(-|)\d{4}(-|)\d{4}$", _input) else "Invalid"
    if out == "Valid":
        out = "Invalid" if re.search(r"(.)\1{3,}", _input.replace("-", "")) else "Valid"
    print(out)
