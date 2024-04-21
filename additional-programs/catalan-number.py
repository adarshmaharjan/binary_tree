"""

Program for nth Catalan Number

Base condition for the recursive approach, when n <= 1, return 1
Iterate from i = 0 to i < n
- Make a recursive call catalan(i) and catalan(n – i – 1) and keep adding the  product of both into res.
Return the res.

"""


def catalan(n):
    if n <= 1:
        return 1

    res = 0

    for i in range(n):
        res += catalan(i) * catalan(n - i - 1)
    return res


for i in range(10):
    print(catalan(i), end=" ")
