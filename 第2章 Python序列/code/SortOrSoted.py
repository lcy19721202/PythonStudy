# -*- coding: cp936 -*-
persons=[{'name':'Dong','age':37},{'name':'Zhang','age':40},{'name':'Li','age':50},{'name':'Dong','age':43}]
print persons
#ʹ��key��ָ���������ݣ��������˼���Ȱ�������������������ͬ�İ����併������
print sorted(persons,key=lambda x:(x['name'],-x['age']))



#sorted����������ɵ������󣬶�sortһ�㳣�����б�
a=(3,5,3,2,1,6,8)
#a.sort()#����Ԫ�����û��sort����
print sorted(a)



#sorted�����������б�ԭ�б��䣻sort����ֱ���޸�ԭ�б���������ֵΪNone
a=[1,3,6,2,3,9,10,7]
print sorted(a)
print a
print a.sort()
print a




#����sort��sorted���ԣ���key����ֻ����һ�Σ���cmp��������ö�Σ���˽�������ʹ��key����
from timeit import Timer
print Timer(stmt='sorted(xs,key=lambda x:x[1])',setup='xs=range(100);xs=zip(xs,xs);').timeit(10000)
print Timer(stmt='sorted(xs,cmp=lambda a,b:cmp(a[1],b[1]))',setup='xs=range(100);xs=zip(xs,xs);').timeit(10000)



#ʹ��sorted���ֵ��������
phonebook = {'Linda':'7750','Bob':'9345','Carol':'5834'}
from operator import itemgetter
sorted_pb=sorted(phonebook.iteritems(),key=itemgetter(1))#���԰�1�ĳ�0�������
print sorted_pb



#ʹ��sorted�Զ�ά�б�����
gameresult = [['Bob',95.0,'A'],['Alan',86.0,'C'],['Mandy',83.5,'A'],['Rob',89.3,'E']]
print sorted(gameresult,key=itemgetter(0,1))#���Ըı�����������ֿ������



#ʹ��sorted�Ժ����б���ֵ�����
mydict={'Li':['M',7],
        'Zhang':['E',2],
        'Wang':['P',3],
        'Du':['C',2],
        'Ma':['C',9],
        'Zhe':['H',7]}
print sorted(mydict.iteritems(),key=lambda (k,v):itemgetter(1)(v))#��(1)(v)�ĳ�(0)(v)��(0)(k)�������



#ʹ��sorted�Ժ����ֵ���б�����
gameresult = [{'name':'Bob','wins':10,'losses':3,'rating':75.0},
              {'name':'David','wins':3,'losses':5,'rating':57.0},
              {'name':'Carol','wins':4,'losses':5,'rating':57.0},
              {'name':'Patty','wins':9,'losses':3,'rating':72.8}]
print sorted(gameresult,key=itemgetter('wins','name'))
