#!/opt/local/bin/python
# -*- coding: utf-8 -*-

import random

a = [random.randint(1,100) for i in range(1,10)]
print(a)
print(max(a), min(a), sum(a), len(a))
print(sum(a)/len(a))
