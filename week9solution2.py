filename = 'problems.txt'

for one_line in open(filename):
    problem = one_line[5:38]
    print(f"{one_line[:38]} = {eval(problem):4}")
