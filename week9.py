import random


def rand_forty():
    for x in range(20):
        return "( " + str(random.randint(-40,40)) + ")"
    
randop = [" - ", " + "]

file = open('mathProblems.txt','w')

for x in range(100):
    file.write("[ " + str(x+1) + "] " + rand_forty() + random.choice(randop) +  rand_forty() + 
            random.choice(randop) + rand_forty() + random.choice(randop) + rand_forty() + " = ________\n")
file.close()
