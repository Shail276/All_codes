#1. Write a Python script to sort (ascending and descending) a dictionary by value.

'''
import operator
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

sorted_by_first_element = sorted(x.items(), key=operator.itemgetter(0))
sorted_by_second_element = sorted(x.items(), key=operator.itemgetter(1))

print sorted_by_first_element, sorted_by_second_element

'''                                                                                  

#2. Write a Python script to add a key to a dictionary.

'''
x = { 'shail': '4'}
x['shah'] = 5

print x

'''

#3. Write a Python script to concatenate following dictionaries to create a new one

'''
dic1={1:10, 2:20} 
dic2={3:30, 4:40} 
dic3={5:50,6:60}

dic4 = dict(dic1.items() + dic2.items() + dic3.items())

print dic4

'''

#4. Write a Python script to check if a given key already exists in a dictionary

'''
z = input('Enter the key')
x = {1:10, 2:20}
if x.has_key(z) == True:
    print 'The key exits'
else:
    print 'It doesnt exists'

'''
#5 Write a Python program to iterate over dictionaries using for loops

'''
x = {1:10, 2:20} 

for keys, value in x.items():
    print (keys, '>' , value)

'''


#6 .Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
'''
def number(y):

    d = dict()
    for i in range(1,y+1):

        d[i] = i*i

    return d
z = number(5)
print z
'''

#7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys

'''
def number(y):

    d = dict()
    for i in range(1,y+1):

        d[i] = i*i

    return d
z = number(15)
print z

'''

#8 Merge 2 python dictionaries
'''
a = {1:10}
b = {2:20}

z = dict(a.items() + b.items())
print z 

'''


#9 iterrate dict
'''
x  = {1:10,2:10,3:30}

for key, values in x.items():
    print (" Key is '%d' and Value is '%d' " % (key, values))

'''


#10. Write a Python program to sum all the items in a dictionary.
'''
x  = {1:10,2:10,3:30}
sum = 0
for key, values in x.items():
    sum += key + values

print sum

'''

#1111. Write a Python program to multiply all the items in a dictionary.

'''
x  = {1:10,2:10,3:30}
ans = 1

for key, values in x.items():
    ans *= key * values

print ans

'''

#delete key pair


'''
x  = {1:10,2:10,3:30}
del x[2]
print x
'''

#13. Write a Python program to map two lists into a dictionary

'''
a = [1,3,5]
b = [6,5,4]
c = dict(zip(a,b))
print c

'''
#14 14. Write a Python program to sort a dictionary by key.

'''
import operator
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

sorted_by_first_element = sorted(x.items(), key=operator.itemgetter(0))
sorted_by_second_element = sorted(x.items(), key=operator.itemgetter(1))

print sorted_by_first_element, sorted_by_second_element

'''

#15 Write a Python program to get the maximum and minimum value in a dictionary.
'''
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
z = max(x)
print z
'''

#17. Write a Python program to remove duplicates from Dictionary.


#18 Write a Python program to check a dictionary is empty or not

'''
x = {}
#y = {}

if len(x) > 0:
    print 'Dict has components'
else:
    print 'Dict is empty'

''' 

#19. Write a Python program to combine two dictionary adding values for common keys

'''
d3['a'] = d1['a'] + d2['a']
print d3
'''
'''
#from collections import Counter
import collections

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d = collections.Counter(d1) + collections.Counter(d2)
print(d)
'''


#20 #20 Write a Python program to print all unique values in a dictionary.

#Sample_Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
'''
d1 = [{"abc":"movies"}, {"abc": "sports"}, {"abc": "music"}, {"xyz": "music"}, {"pqr":"music"}, {"pqr":"movies"},{"pqr":"sports"}, {"pqr":"news"}, {"pqr":"sports"}]

#d1 = {'a': 100, 'b': 200, 'c':300}

s = set()

for dic in d1:
	for val in dic.values(): 
		s.add(val)

for x in s:
	print x
'''


# Program using dict.values() 

'''
d1 = {'a': 100, 'b': 200, 'c':300}
print 'Value is "%s"' % d1.values()

'''

#21 Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary. Go to the editor
#Sample data : {'1':['a','b'], '2':['c','d']}
#Expected Output: ac ad bc bd
'''
x = {'1':['a','b'], '2':['c','d']} 
y = x.values()
#print y
w = []

for i in y:
	for j in i:
		w.append(j)
#print w

for k in w:
	print 'a' + 'b'
	print 'a' + 'c'
'''

'''
import itertools

x = {'1':['a','b'], '2':['c','d']} 

for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
    print(''.join(combo))

'''


#24 24. Write a Python program to create a dictionary from a string.




#25 25. Write a Python program to print a dictionary in table format.
'''

from collections import defaultdict, Counter

str1 = 'w3resource' 

my_dict = {}

for letter in str1:
    my_dict[letter] = my_dict.get(letter, 0) + 1

print(my_dict)

'''

#26Write a Python program to count the values associated with key in a dictionary.

'''
student = [{'id': 1, 'success': True, 'name': 'Lary'},
 {'id': 2, 'success': False, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'}]

count = 0

for d in student:
 	if d['success'] == True:
 		count += 1

print count

'''


#27 Write a Python program to convert a list into a nested dictionary of keys.
'''
num_list = [1, 2, 3, 4]
new_dict = current = {}
for name in num_list:
    current[name] = {}
    print current
    current = current[name]
    print current
print(new_dict)
'''
