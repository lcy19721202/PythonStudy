# -*- coding: cp936 -*-

#�б����֧�ֶ���Ƕ��
nested_list = [['Hello','World'],['Goodbye','World']]
print [[s.upper() for s in xs] for xs in nested_list]


#�б����֧�ֶ��ص���
print [(a,b) for a in ['a',1,'c'] for b in [1,2,'c',4,'a'] if a !=b]


#�б����֧�ָ��ӱ��ʽ
def f(v):
    if v%2 == 0:
        v=v**2
    else:
        v=v+1
    return v
print [f(v) for v in [2,3,4,-1] if v>0]
print [v**2 if v%2 == 0 else v+1 for v in [2,3,4,-1] if v>0]


#�б����֧������ɵ�������
fp = open('c:\install.log','r')
print [i for i in fp if 'c:' in i]
fp.close()
