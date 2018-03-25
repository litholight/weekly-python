
import hashlib
import os

class DirFileHash(object):

    def __init__(self, directory):
        if os.path.isdir(directory):
            self.directory = directory
        else:
            print("This is not a valid directory: %s" %directory)
        
    def __getitem__(self, fileToHash):
        try:
            with open(os.path.join(self.directory, fileToHash),'rb') as f:
                return(hashlib.md5(f.read()).hexdigest())
        except(FileNotFoundError, TypeError):
            return None

#directory = "./"
#d = DirFileHash(directory)
#print(d["redditbot.py"])
