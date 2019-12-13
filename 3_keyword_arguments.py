'''
1. We can pass values based on parameter name.
2. Keyword arguments should follow positional argument.
'''
def add(a,b):
    print(' A value is :', a)
    print(' B value is :', b)
    print(a + b)

add(b=4,a=78)

#add(4,a=78)

#add(b=4,78)

#add(4, 7)

# Error:
# SyntaxError: positional argument follows keyword argument