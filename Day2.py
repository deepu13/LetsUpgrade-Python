# Question 1:
# List and its default methods

lst = ['apple',13,26.0,[1,2,3]]
print(lst)
# output : ['apple', 13, 26.0, [1, 2, 3]]

# method 1 : append()
lst.append('mango')
print(lst)
# output : ['apple', 13, 26.0, [1, 2, 3], 'mango']

# method 2 : count()
print( lst.count(13) )
# output : 1

# method 3 : index()
print(lst.index('mango'))
# output : 4

# method 4 : pop()
lst.pop(4)
print(lst)
# output : ['apple', 13, 26.0, [1, 2, 3]]

# method 5 : insert()
lst.insert(3,'orange')
print(lst)
# output : ['apple', 13, 26.0, 'orange', [1, 2, 3]]

# **********************************************************************************

# Question 2:
# Dictionary and its default functions

dct = {'a':1 ,'b':2 , 'c':3 , 'd':4}
print(dct)
# output : {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# method 1 : items()
print(dct.items())
# output : dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4)])

# method 2 : get()
print(dct.get('b'))
# output : 2

# method 3 : keys()
print(dct.keys())
# output : dict_keys(['a', 'b', 'c', 'd'])

# method 4 : pop()
dct.pop('b')
print(dct)
# output : {'a': 1, 'c': 3, 'd': 4}

# method 5 : values()
print(dct.values())
# output : dict_values([1, 3, 4])

# **********************************************************************************

# Question 3:
# Sets and its default functions

st = {'sat','sun','mon'}
print(st)
# output : {'mon', 'sat', 'sun'}

# method 1 : update()
st.update(['thu','fri'])
print(st)
# output : {'sat', 'fri', 'thu', 'sun', 'mon'}

# method 2 : remove()
st.remove('sun')
print(st)
# output : {'sat', 'fri', 'thu', 'mon'}

# method 3 : add()
st.add('sun')
print(st)
# output :{'sat', 'fri', 'thu', 'sun', 'mon'}

# method 4 : union()
st2 = {'tue','wed','thu'}
st3=st.union(st2)
print(st3)
#output : {'tue', 'sat', 'fri', 'sun', 'mon', 'thu', 'wed'}

# method 5 : len()
print(len(st3))
# output : 7

# **********************************************************************************

# Question 4:
# Tuple and its default methods

tpl = ('red','yellow','green','blue','red')
print(tpl)
# output : ('red', 'yellow', 'green', 'blue', 'red')

# method 1 : index()
print(tpl.index('blue'))
# output : 3

# method 2 : count()
print(tpl.count('red'))
# output : 2

# **********************************************************************************

# Question 5:
# Strings and its default methods

py = "python is fun learning"
print(py)
# python is fun learning

# method 1 : index()
print(py.index('fun'))
# output : 10

# method 2 : islower()
print(py.islower())
# output : True

# method 3 : count()
print(py.count('i'))
# output : 2

# method 4 : split()
print(py.split(" "))
# output : ['python', 'is', 'fun', 'learning']

# method 5: upper()
print(py.upper())
# output : PYTHON IS FUN LEARNING

# **********************************************************************************