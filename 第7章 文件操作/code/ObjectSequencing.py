# -*- coding: cp936 -*-
#���л����򵥵�˵���ǰ��ڴ��е����ݽṹ�ڲ���ʧ����ݺ�������Ϣ�������ת�ɶ�����ı�������Ʊ�ʾ�Ĺ��̣�
#�������л������ʽ���������л�����Ӧ���ܹ��ָ�Ϊԭ����
#Python�г��õ����л�ģ����pickle��json��marshal��shelve
#����pickle��C����ʵ�ֵ�cPickle���ٶ�Լ���1000����cPickle���ܱ����ɣ�����Ӱ������Ӧ��


#�Ƽ�����ʹ��cPickle����Linux�����л��ĸ�ʽ�ļ�������Windowsƽ̨�Ͻ��з����л�
import cPickle as pickle
data = {'name':'Dong Fuguo','Age':37,'affiliate':'SDIBT'}
print data
fp=open('pickletest.dat','wb')
pickle.dump(data,fp)
fp.close()

with open('pickletest.dat','rb') as f:
    print pickle.load(f)


#pickle�ܹ��Զ�ά�����������ã����һ�������ϴ��ڶ�����ã�pickle�󲻻�ı���������ã�
#�����ܹ��Զ�����ѭ���͵ݹ�����
a=['a','b']
b=a
b.append('c')
p=pickle.dumps((a,b))
a1,b1=pickle.loads(p)
print a1
print b1
a1.append('d')
print b1
