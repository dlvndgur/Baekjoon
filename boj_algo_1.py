import numpy as np
from random import randint 

def method1():
    print('this is method 1')
    for i in range(10):
        print('*' * (10-i))


def method2():
    print('this is method 2')
    li = np.array([randint(1,100) for _ in range(randint(1,100))])
    print(li, '\nlength of li : ', len(li))

def method3():
    s = set()
    while len(s) <= 20:
        s.add(randint(1, 100))
    print(s)

if __name__ == '__main__':
    method1()

    method2()
    print('왜 안되냐고')