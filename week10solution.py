
letters = 'abcde'
numbers = [1,2,3,4,5]
symbols = '!@#$%'

def multiziperator(*args):
    for one_index in zip(*args):
        for one_element in one_index:
            yield one_element

for one_item in multiziperator(letters, numbers, symbols):
   print(one_item)

