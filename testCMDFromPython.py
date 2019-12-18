import os
from multiprocessing import Pool


import multiprocessing

NUMBER_OF_SESSIONS = 5

def worker():
    while True:
        os.system("dir")


if __name__ == '__main__':
    jobs = []
    for i in range( NUMBER_OF_SESSIONS ):
        p = multiprocessing.Process(target=worker)
        jobs.append(p)
        p.start()
'''        
with Pool(5) as p:
    os.system("cmd /k 'cd'")
'''