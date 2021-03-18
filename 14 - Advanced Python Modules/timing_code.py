def func_one(n):
    return [str(num) for num in range(n)]

print(func_one(10))

def func_two(n):
    return list(map(str,range(n)))

print(func_two(10))


import time
# Current time before code
start_time = time.time()

# running code
result = func_two(1000000)

# Current time after code
end_time = time.time()

# Elapsed Time
elapsed_time = end_time - start_time

print(elapsed_time)


import timeit


stmt = '''
func_one(100)
'''

setup = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''

x = timeit.timeit(stmt, setup, number=1000000)
print(x)
