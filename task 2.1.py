def square_generetor(n):
    for i in range(n+1):
        yield i * i

def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield str(i)

def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

a, b = 3, 7
for square in squares(a, b):
    print(square)

def countdown(n):
    for i in range(n, -1, -1):
        yield i








