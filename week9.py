import random


def rand_forty():
    for x in range(20):
        return "( " + str(random.randint(-40,40)) + " )"

    
randop = [" - ", " + "]
   




for x in range(100):
    print(rand_forty() + random.choice(randop) +  rand_forty() + random.choice(randop) + rand_forty() + random.choice(randop) + rand_forty())
