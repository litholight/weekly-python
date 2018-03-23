
import sys

class Tee(object):
    def __init__(self, *files):
        self.files = files

    def write(self, text):
        for one_file in self.files:
            one_file.write(text)

    def writelines(self, lines):
        for one_file in self.files:
            one_file.writelines(lines)
    
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        for one_file in self.files:
            one_file.close()

f1 = open('open1.txt', 'w')
f2 = open('open2.txt', 'w')

with Tee(f1, f2) as t:
    t.write('In the beginning..\n')
    t.write('God created the heavens and the earth.\n')
