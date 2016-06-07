# 位置参数
def power(x):
    return x * x

def power(x,n):
    s = 1
    while n > 0 :
        n = n - 1
        s = s * x
    return s

# default parameter
def power(x,n = 2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

#从上面的例子可以看出，默认参数可以简化函数的调用。设置默认参数时，有几点要注意：
#一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；
#二是如何设置默认参数。
#当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。


# Wrong
def add_end(L = []):
    L.appemd('End')
    return L
# Right
def add_end(L = None):
    if L is None:
        L = []
    L.append("END")
    return L

#
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc([1,2,3,4,5,6]))
#  可变函数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc(1,2,3,4,5))

# 关键字参数
def person(name, age, **kw):
    print(name, age, kw)

print(person("fuck",24))
print(person("hey",47, city = "gz", gender = "male"))
extra = {'city' : 'Beijing', 'job': 'student' }
print(person("what",23,**extra))