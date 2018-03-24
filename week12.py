
import hashlib
import os

class DirFileHash():

    def __init__(self, directory):
        self.theseFiles = os.listdir(directory)
        
    def __getitiem__(self, theseFiles, fileToHash):
        filesHashDir = {}

        for each_file in theseFiles:
            m = hashlib.md5()
            f = open(each_file,'r')
            fr = f.read()
            fhash = update(fr.encode('utf-8'))
            print(each_file) 
            if fileToHash == each_file:
                print(fhash)
                break


#m2 = hashlib.md5()
#f1 = open("open1.txt", 'r')
#bibleverse = f1.read()
#m2.update(bibleverse.encode('utf-8'))
#print(m2.digest())
#f1.close()

d = DirFileHash("/")
d[redditbot.py]
