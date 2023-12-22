'''
Author: your name
Date: 2021-04-18 21:58:43
LastEditTime: 2021-04-18 21:58:43
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \excelDataProc\test.py
'''
import pandas as pd 
from pandas import DataFrame, Series
data = DataFrame({'name':['yang', 'jian', 'yj'], 'age':[23, 34, 22], 'gender':['male', 'male', 'female']})
#data数据
'''
In[182]: data
Out[182]: 
   age  gender  name
0   23    male  yang
1   34    male  jian
2   22  female    yj
'''
#删除gender列，不改变原来的data数据，返回删除后的新表data_2。axis为1表示删除列，0表示删除行。inplace为True表示直接对原表修改。
data_2 = data.drop('gender', axis=1, inplace=False)
'''
In[184]: data_2
Out[184]: 
   age  name
0   23  yang
1   34  jian
2   22    yj
'''
#改变某一列的位置。如：先删除gender列，然后在原表data中第0列插入被删掉的列。
data.insert(0, '性别', data.pop('gender'))#pop返回删除的列，插入到第0列，并取新名为'性别'
'''
In[185]: data
Out[186]: 
       性别  age  name
0    male   23  yang
1    male   34  jian
2  female   22    yj
'''
#直接在原数据上删除列
del data['性别']
'''
In[188]: data
Out[188]: 
   age  name
0   23  yang
1   34  jian
2   22    yj
'''