import random
import collections
from random import randint
from collections import Counter
import math
l=[randint(0,10) for i in range(20)]
maks=0
st=0
nd=0
rd=0
th4=0
th5=0
for i in range(len(l)):
    print(l[i], ' [',i,'] ')
for i in range(len(l)-5):
    temp=l[i]+l[i+1]+l[i+2]+l[i+3]+l[i+4]
    if (temp)>maks:
        maks=temp
        st=l[i]
        sti=i
        nd=l[i+1]
        ndi=i+1
        rd=l[i+2]
        rdi=i+2
        th4=l[i+3]
        th4i=i+3
        th5=l[i+4]
        th5i=i+4
print('1st ',st,'[',sti,']',' 2nd ',nd,'[',ndi,']',' 3rd ',rd,'[',rdi,']',' 4th ',th4,'[',th4i,']', ' 5th ',th5,'[',th5i,']' )
