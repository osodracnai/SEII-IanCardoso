#Ian Cardoso
#11411EMT014

x = 'global x'

def test():
    y = 'local y'
    x = 'local x'
    print(y)
    print(x)
    
test()
print(y)
print(x)
   
import builtins

def my_min ():
    pass

m = min ([5, 1, 4, 2, 3])
print(m)


def outer():
    x = 'outer x'

    def inner():
        x = 'inner x'
        print(x)

    inner()
    print(x)

outer()
print(x)
