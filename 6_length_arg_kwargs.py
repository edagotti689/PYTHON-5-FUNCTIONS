'''
1. using kwargs(**) we can takes values in dictionary format
'''
def add(a, b=5,*c, **d):
    print(' A value is : ', a)
    print(' B value is : ', b)
    print(' C value is : ', c)
    print(' D value is : ', d)

add(6,7,67,9, name='sriram', eid=56)



'''

https://www.geeksforgeeks.org/args-kwargs-python/

about kwargs 
'''
