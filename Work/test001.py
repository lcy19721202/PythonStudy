#!/opt/local/bin/python
# -*- coding: utf-8 -*-

#import io
#import sys
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')


for letter in 'Python':     # 第一个实例
   print(letter,end='\t')

print("\n换行",end='\n')

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 第二个实例
   print(fruit,end='\t')

print("\nGood bye!",end='\n')

for i in (3, 5, 7):  print(i, end='\t')


