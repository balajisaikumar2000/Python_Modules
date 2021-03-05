from contextlib import contextmanager
import os
"""
class Open_File():
    def __init__(self,filename,mode):
        self.filename = filename
        self.mode =  mode
    def __enter__(self):
        self.file = open(self.filename,self.mode)
        return self.file
    def __exit__(self,exc_type,exc_val,traceback):
        self.file.close()
with Open_File("sample.txt","w") as f:
    f.write("Testing")
print(f.closed)              """

@contextmanager
def open_file(file,mode):
    f = open(file,mode)
    yield f
    f.close()

with open_file("sample.txt","w") as f:
    f.write("Lorem ipsu, dolor sit amet ,constructor adipiscing elit")
print(f.closed)
@contextmanager
def change_dir(destination):
    try:
        cwd =os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)
with change_dir("itertools"):
    print(os.listdir())

