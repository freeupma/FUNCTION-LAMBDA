def add(a,b):
    sum=a+b
    return sum
a=int(input('Enter First Number'))
b=int(input('Enter Second Number'))
result=add(a,b)
print('Output=', result)


sum=(lambda x,y:x+y)
a=int(input('Enter First Number'))
b=int(input('Enter Second Number'))
print('Sum=', sum(a,b))
      


def square_function(a):
    return a**2
print(square_function(16))


get_square= lambda a:a**2
print(get_square(256))
