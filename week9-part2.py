
file1 = open('mathProblems.txt', 'r')
file2 = open('mathSolutions.txt', 'w')
for line in file1:
    start = line.find(']')+1
    end = line.find('=')
    one = line[start:end]
    line = line.replace("________\n", " ")
    file2.write(line + str(eval(one)))
    file2.write("\n")
file1.close()
file2.close()

