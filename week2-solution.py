
def myrange2(first, second=None, step=1):
    if second is None:
        current = 0
        end = first
    else:
        current = first
        end = second
        
    output = []
    while current < end:
        output.append(current)
        current += step

    return print(output)

myrange2(10)

myrange2(10,20)

myrange2(10,20,2)

