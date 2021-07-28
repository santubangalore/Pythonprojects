

from array import *

vals = array('i',[5,9,8,4,3])

newArr = array(vals.typecode, (a*a for a in vals))

for a in newArr:
    print(a)

