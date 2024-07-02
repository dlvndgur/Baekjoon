import numpy as np
from random import randint 

def method1():
    print('this is method 1')

def method2():
    print('this is method 2')
    li = np.array([randint(1,100) for _ in range(randint(1,100))])
    print(li, '\nlength of li : ', len(li))

def method3():
    for _ in range(10):
        for i in range(10):
            print('*' * i)

if __name__ == '__main__':
    print('여기는 method3 branch 입니다.')
    method1()

    method2()

    method3()