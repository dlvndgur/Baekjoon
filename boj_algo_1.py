import numpy as np
from random import randint 

def method1():
    print('this is method 1')
    method2()

def method2():
    print('this is method 2')
    li = np.array([randint(1,100) for _ in range(randint(1,100))])
    print(li, '\nlength of li : ', len(li))

if __name__ == '__main__':
    method1()