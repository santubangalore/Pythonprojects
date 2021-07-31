
from numpy import *

n1 = matrix('1 2 3; 6 4 5; 1 6 7')
n2 = matrix('1 2 3; 6 8 5; 2 6 7')

n3 = n1*n2


print (diagonal(n3))
