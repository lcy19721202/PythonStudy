#!/opt/local/bin/python
# -*- coding: utf-8 -*-

from functools import reduce


def add(x, y):
  return x + y


def add5(v):
  return v + 5


def func(x):
  return x.isalnum()


print(list(map(add5, range(10))))
print(list(map(add, range(5), range(5, 10))))

seq1 = list(range(1, 10))
seq2 = reduce(lambda x, y: x + y, seq1)
print(seq1)
print(seq2)

seq = ['foo', 'x41', '?!', '***']
print(list(filter(func, seq)))  # 把filter对象转换为列表

print(list(zip('123', 'abc', ',.!')))

fp = open(r'/tmp/test.txt', 'a+')
print('Hello,world!', file=fp)
fp.close()

for i in range(10, 20):
  print(i, end=' ')

'''
注释
'''
print('\n')

"""
注释
"""
z = input('Please input:')
print(type(z))
