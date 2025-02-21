def even_n(n):
    for i in range(0, n):
        if i % 2 == 0:
            yield i 

n = int(input())

print("even numbers:", "," . join(map(str, even_n(n))))