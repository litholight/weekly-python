import os
from collections import defaultdict

def file_function(directory, any_file_func):
    success_dict = {}
    failure_dict = {}
    for filename in os.listdir(directory):
        try:
            success_dict[filename] = any_file_func(directory + filename)
        except Exception as ex:
            failure_dict[filename] = ex
    return success_dict, failure_dict

def file_length(filename):
    size = os.stat(filename).st_size
    return size

directory = "./"

success_dict, failure_dict = file_function(directory, file_length)

print("Filenames and the function result")
for k,v in success_dict.items():
    print(k, ":", v)

print("Filenames and exception number:")
for k,v in failure_dict.items():
    print(k, ":", v)

