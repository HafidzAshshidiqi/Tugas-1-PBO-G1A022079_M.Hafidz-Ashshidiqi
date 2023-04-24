def kalkulator_persegi(n):
    return n**2

numbers = [1, 2, 3, 4, 5]
persegi = list(map(kalkulator_persegi, numbers))
print(persegi) # output: [1, 4, 9, 16, 25]
