"""
Example of recursion using the factorial
"""


def rec_fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * rec_fatorial(n - 1)


num = int(input("Digite um número: "))
print("O fatorial de ", num, " é ", rec_fatorial(num))
