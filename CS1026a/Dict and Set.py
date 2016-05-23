names = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(names['Michael'])

names['Adam'] = 67
print(names)

names['Adam'] = 80
print (names)

isKeyIn = 'Adam' in names
print(isKeyIn)

isKeyIn = names.get('Yijun')
isKeyIn = names.get('Yijun', 85)
score = names.get('Adam')
print(isKeyIn, score)

names.pop('Bob')
print(names)

key = (1,2,3)
names[key] = 'fuck'
print(names[key])

# set
s = set([1,2,3])
print(s)

s.add(4)
print(s)
s.remove(4)
print(s)

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1&s2, s1|s2)

# 不可变对象

a = 'abc'
print(a.replace('a','A'))
print(a)

b = a.replace('a','A')
print(b,a)
# replace does not change the variable a, it just return a new value
