
def myrange2(minim, maxim=0, step=1):
    listOfNumbers = []
    if maxim == 0 and minim > 0:
        maxim = minim
        minim = 0
    x = minim
    while x < maxim and x >= minim:
        listOfNumbers.append(x)
        x += step
    return listOfNumbers

def myrange3(minim, maxim=0, step=1):
    if maxim == 0 and minim > 0:
        maxim = minim
        minim = 0
    x = minim
    while x < maxim and x >= minim:
        yield x
        x += step

print("myrange2:")
for x in myrange2(10, 30, 3):
    print(x)

print("\nmyrange3:")
for x in myrange3(10, 30 ,3):
    print(x)
