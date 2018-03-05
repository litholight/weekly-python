import random

number_source = range(-40,40)
sign_source = ['+','-']*4
filename = 'problems.txt'

with open(filename, 'w') as f:
    for i in range(1, 101):
        signs = random.sample(sign_source,3)
        numbers = random.sample(number_source, 4)

        f.write(f"[{i:3}] {numbers[0]:4} {signs[0]} ({numbers[1]:4}) {signs[1]} ({numbers[2]:4}) {signs[2]} ({numbers[3]:4}) = _____\n") 
