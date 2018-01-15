
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

def myrange3(first, second=None, step=1):
    if second is None:
        currrent = 0
        end = first
    else:
        current = first
        end = second

    while current < end:
        yield current
        current += step

list(myrange3(10))

list(myrange3(10,20))

list(myrange3(10,20,2))

