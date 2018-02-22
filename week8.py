import os
from collections import defaultdict

def file_length(directory):
    filelength = defaultdict()
    for filename in os.listdir(directory):
        size = os.stat(filename).st_size
        filelength[filename] = size
    print(filelength)

file_length("./")

#filename = "week7printout.txt"
#print(os.stat(filename).st_size)
