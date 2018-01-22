
def logtodict(filename):
    return[{'':''}
            for line in open(filename)]

print(logtodict('mini-access-log.txt'))
