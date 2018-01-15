
def myrange2(first, second=None, step=1):
    if second is None:
        current = 0
        end = first
    else:
        current = first
        end = second
    print("first = {}".format(current))
    print("second = {}".format(end))
    print("step = {}".format(step))

myrange2(10)

myrange2(10,20)

myrange2(10,20,2)

