a = int(input('a = '))
b = int(input('b = '))

import math
a = a*b
b = math.pow(b/a,-1)
a = a/b

print('a =',int(a))
print('b =',int(b))