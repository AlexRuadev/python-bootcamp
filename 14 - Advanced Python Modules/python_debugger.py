x = [1,2,3]
y = 2
z = 3


# Import python debugger

import pdb

result = y + z

# setitng our trace before the error line, we can then trying to debug finding what's the error
pdb.set_trace()
result2 = x + y

