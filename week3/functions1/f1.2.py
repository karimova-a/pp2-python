def cent(fahr):

    cent = (5 / 9) * (fahr - 32)

    return cent


x = float(input())

centi = cent(x) 

print(f"{x} Fahrenheit is equal to {centi:.2f} Centigrade")