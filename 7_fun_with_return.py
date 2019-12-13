'''
1. Return keyword used to return value from function.
2. After executing return keyword function will terminate
3. We can use many return keywords in side a function
'''

def add(a=20,b=30):
    print('Before return')
    return a + b
    print('After return')

ret = add()

print(' return value is :', ret)




