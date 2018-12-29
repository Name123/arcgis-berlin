import os


def makedirs(dirs):
    for d in dirs:
        try:
            os.mkdir(d)
        except FileExistsError:
            pass
        
    
