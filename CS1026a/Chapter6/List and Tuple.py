classmate = ['what','the','fuck']
for i in range(len(classmate)):
    print(classmate[i])
for names in classmate:
    print(names)
classmate.append('oh year')
classmate.insert(1, 'what are you saying')
print(classmate)
classmate.pop(2)
print(classmate)
classmate[2] = 'What the hell'
print(classmate)
L = ['apple', 12312, True]
print(L)
s = ['python','java', ['asp','php'], 'scheme']
print(len(s))

number = list(range(5))
print(number)


# tuple
classmate = ('what', 's', 'up')
print(classmate[2])
t = (1,)
print(t)
t = ('a','b',['A','B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)

