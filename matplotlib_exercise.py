#!/usr/bin/python
'''
1-50共50个数中，每次取走其中两个数求两个数的差的绝对值，将结果放回其中，问最后一次操作完后，剩下的数字可能是多少？
'''

import matplotlib.pyplot as plt
import random

def last_number():
    l =range(1,51)
    while len(l) >1:
        random.shuffle(l)
        l.append(abs(l.pop()-l.pop()))
    return l[0]

number = {}
for i in xrange(100000):
    save = last_number()
    if save in number:
        number[save] += 1 
    else :
        number[save] = 1 

print number        
        
x = number.keys()
y = [number[i] for i in x]

plt.plot(x,y,color='red', linestyle='dashed', marker='o')
plt.show()

'''
运行十万次的结果
{1: 13012, 3: 11731, 5: 10625, 7: 9232, 9: 8321, 11: 7311, 13: 6553, 15: 5674,
7: 4861, 19: 4260, 21: 3637, 23: 3074, 25: 2558, 27: 2207, 29: 1731, 31: 1433,
3: 1070, 35: 849, 37: 660, 39: 457, 41: 328, 43: 201, 45: 133, 47: 60, 49: 22}
'''