import math


func = lambda x: math.floor(x / 3) - 2

def fuel_list(x):
    fuel = func(x)
    while fuel > 0:
        yield fuel
        fuel = func(fuel)

f = open("input")

print(sum(map(lambda x: sum(fuel_list(int(x))), f)))
