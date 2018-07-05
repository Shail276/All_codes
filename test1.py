'''

import re
my_regex_str = "Ethernet Routing Switch 3549GTS-PWR+"
a = re.findall(r"(.{5}).+ (.+?)\s(\d{2,4}).+-(.{4})", my_regex_str)
z=a[0][2]
print z
print x
'''


'''
import re
def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)

print(is_allowed_specific_char("ABCDEFabcdef123450")) 
print(is_allowed_specific_char("*&%@#!}{"))

'''

'''
import re
string = '22.22.22.1     0      b4:a9:5a:ff:c8:45    VLAN#222     L'
a = re.search(r"(.+?) +(\d) +(.+?)\s{2,}(\w)*", string)

b = re.findall(r"\d\d\.\d{2}\.[0-9][0-9]\.[0-9]{1,3}", string)

#output = ['22.22.22.1']


'''
'''
import re

def text_matching(text):
    
    pattern = 'ab*?'
    if re.search(pattern, text):
        return ('match found')
    else:
        return ('Not found')

z = text_matching('ac')
print (z)
x = text_matching('abc')
print (x)
w = text_matching('abbbc')
print (w)


#3
import re

def text_matching(text):
    
    pattern = 'ab+?'
    if re.search(pattern, text):
        return ('match found')
    else:
        return ('Not found')

z = text_matching('ac')
print (z)
x = text_matching('abc')
print (x)
w = text_matching('abbbc')
print (w)


#4

import re

def text_matching(text):
    
    pattern = 'ab{3}'
    if re.search(pattern, text):
        return ('match found')
    else:
        return ('Not found')

z = text_matching('ac')
print (z)
x = text_matching('abc')
print (x)
w = text_matching('abbbc')
print (w)


#5

import re

def text_matching(text):
    
    pattern = 'ab{3}?'
    if re.search(pattern, text):
        return ('match found')
    else:
        return ('Not found')

z = text_matching('ac')
print (z)
x = text_matching('abc')
print (x)
w = text_matching('abbb')
print (w)

#6

import re

def text_matching(text):
    
    pattern = 'ab{2,3}?'
    if re.search(pattern, text):
        return ('match found')
    else:
        return ('Not found')

z = text_matching('ac')
print (z)
x = text_matching('abc')
print (x)
w = text_matching('abbb')
print (w)


#7
'''
'''
import re
def text_match(text):
        patterns = '[a-z]+_$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("Aaaa"))
print(text_match("ADaabAbbbc_"))
print(text_match("Aaab_abbbc"))
'''

#8
'''
import re
def text_match(text):
        patterns = '^[A-Z][a-z]+?$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("aab_cbbbc"))
print(text_match("aab_Abbbc"))
print(text_match("Aaab_abbbc"))

'''


#9

'''
import re
def text_match(text):
        patterns = '^a.+?b$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("a&-bb"))
print(text_match("aab_Abbbc"))
print(text_match("Aaab_abbbc"))

'''


#10
'''
import re
def text_match(text):
        patterns = '^\w+?'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return'Not matched!'

print(text_match("shail shah"))
print(text_match(" 	676767"))
print(text_match("fsdfsf"))

'''

#11
'''
import re
def text_match(text):
        patterns = '\w\S*$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("aab_cbbbc."))
print(text_match("aab_Abbbc "))
print(text_match("Aaab_abbbc "))
'''

#12
'''

import re
def text_match(text):
        patterns = '\w*z.\w*'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("ezbra is black"))
print(text_match("skhdkahkd  zebra jhaksdk"))
print(text_match("Aaab_abbzbc"))
'''

#13

'''
import re
def text_match(text):
        #patterns = '\Bz\B'
        #patterns = '\bz\b'
        patterns = '\w+z+\w+'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match(" azd"))
print(text_match("aab_Abbbz"))
print(text_match("Aaab_abbbc"))

'''

#16

'''
import re
ip = '22.08.009.06'
#string = re.sub('\.[0]*','.',ip)
string = re.sub('\.[0]*','.',ip)
print string
'''

#15
'''
import re
string = '5675'

z = re.match('^5',string)
print z

'''

#14


'''
import re
def text_match(text):
        patterns = '^[a-zA-Z_]*$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("a_Z_9 dkfhak"))
print(text_match("%%%%%"))
print(text_match("Aaab_abbbc"))

'''

#17

'''
import re
def text_match(text):
        patterns = '\d$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("adad9"))
print(text_match("%%%%%"))
print(text_match("Aaab_abbbc8"))

'''

#18
'''
import re
def text_match(text):
        patterns = '[0-9]{1,3}'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("a_Z_9 dkfhak"))
print(text_match("%%%%%"))
print(text_match("Aaab_abbbc"))

'''
#19

'''
import re
patterns = [ 'fox', 'dog', 'horse' ]
text = 'The quick brown fox jumps over the lazy dog.'
for pattern in patterns:
    print('Searching for "%s" in "%s" ' % (pattern, text),)
    if re.search(pattern,  text):
        print('Matched!')
    else:
        print('Not Matched!')

'''
#20

'''
import re

pattern = 'fox'
text = 'The quick brown fox jumps over the lazy dog.'
match = re.search(pattern,text)

s = match.start()
e = match.end()

print('Found "%s" in "%s" from "%d" to "%d"' %(pattern,text,s,e))

'''

#21
'''

import re

text = 'Python exercises, PHP exercises, C exercises'
pattern = 'exercises'

if re.findall(pattern, text):
	print 'match found'

'''

#22
'''
import re

text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'

for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print('Found "%s" at "%d:%d"' % (text[s:e], s, e))

'''

'''
import re
text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print('Found "%s" at %d:%d' % (text[s:e], s, e))

'''

#23

# we can also .replace(,) method
'''
import re

string = '_Excerfs _ _ _ _ _'

a = re.sub('_',' ',string)
b = re.sub(' ','_',string)

print a
print b

'''


#24
'''
import re
url1= "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"

z = re.findall(r'/(\d{4})/(\d{1,2})/(\d{1,2})', url1)
print z 
'''

#25
'''
import re
url1= '2016-02-01'

#z = re.findall(r'/(\d{4})/(\d{1,2})/(\d{1,2})', url1)
#yyyy-mm-dd format to dd-mm-yyyy

x = re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', url1)
print x
'''


#26
'''
import re

# Sample strings.
words = ["Python PHP", "Java JavaScript", "c c++"]

for w in words:
        m = re.match("(P\w+)\W(P\w+)", w)
        # Check for success
        if m:
            print(m.groups())
'''

#27
'''
import re
text = "Ten 10, Twenty 20, Thirty 30"

x = re.findall(r'\d+',text)
print x
#for i in x:
#	print i

'''

#28
'''
import re

text = 'shail is asds ewee asas'

x = re.findall('[ae]\w+',text)

y = ','.join(x)
print y

'''

#29
'''
import re
# Input.
text = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."

for m in re.finditer("\d+", text):
    
    print("Index position:", m.start())
    print ("start and end index position", m.span())
# .start() --- displays the start position
# .end() ---- displays the end position
# .span() ---- displays the start and end position. 

'''
'''
'''
#30
'''
import re

text = 'road'

x = re.sub('road','rd',text)
print x
'''

#31
'''
import re
text = 'Python Exercises, PHP exercises.'
print(re.sub("[ ,.]", ":", text))

'''

#32
'''
import re
text = 'Python Exercises,,,PHP exercises'
#print(re.sub("[ ,.]", ":", text,2))

x = re.sub('[ ,.]{2}',':',text)
print x
'''

#33
'''
import re
x = 'hjhdfhksh hfkah frer gfe jhfg'

y = re.findall(r'\b\w{5}\b', x)
print y
'''


#34
'''
import re
x = 'hjf hfkah frere'

y = re.findall(r'\b\w{3,5}\b', x)
print y

#35
'''
'''
import re
x = 'hgh hghfgh hdghfgh hghg'

y = re.findall(r'\b\w{4,}\b',x)
print y
'''

'''
#36
'''
'''
def camel_to_snake(text):
        import re
        str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower()

print(camel_to_snake('PythonExercises'))
'''
#35
'''
import re
x = 'gh hjfgdg hfkah frere'

y = re.findall(r'\b\w{4,}\b', x)
print y

'''
#38
'''
import re
x = 'gh "hjfgdg" hfkah frere'

if re.findall(r'"\w+"',x):
	print 'match found'
else:
	print 'match not found'
'''
'''
#40
import re
x = 'aasdd bfsbf    fsdf' 

y = re.sub('\s','',x)
print(y)

'''

#39
'''
import re
x = 'aasdd bfsbf    fsdf' 

y = re.sub(' +','',x)
print(y)

'''

#40
'''
import re
x = 'aasdd&&&bfsbf%%%%fsdf' 

y = re.sub('\W','',x)
print(y)
'''

#42
'''
import re
text = '<p>Contents :</p><a href="https://w3resource.com">Python Examples</a><a href="http://github.com">Even More Examples</a>'
urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
print("Original string: ",text)
print("Urls: ",urls)

'''

#43
'''
import re
text = "PythonTutorialAndExercises"
print(re.findall('[A-Z][^A-Z]*', text))
'''
#44


#46
'''

import re
text = "Clearly, he has no excuse for such behavior."
for m in re.finditer(r"\w+ly", text):
    print('%d-%d: %s' % (m.start(), m.end(), m.group(0)))
'''
'''
n=int(raw_input()
d=dict()
for x in xrange(1,10):
     i in range(1,n+1):
    d[i]=i*i
'''

'''
n = int(raw_input('enter the num'))
d = {}

for i in range(1,10):
    d[i] = i*i

print d
'''

#50
'''q
import re
Sample_data = ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]

pattern = '?\([^)]+\'

x = re.sub(pattern, ' ' ,Sample_data)
print x
'''




#Leetcode  ####################################################################

#Write a function that takes a string as input and returns the string reversed.
'''
def reverse_a_string_more_slowly(a_string):
    new_strings = []
    index = len(a_string)
    while index:
        index -= 1                       
        new_strings.append(a_string[index])
    return ''.join(new_strings)

x = reverse_a_string_more_slowly('hello')
print x 

'''

#reverse words in a string
'''
x = 'Hello world'
y = x.split(' ')
#print y
new_strings = []

for nam in y:
    index = len(nam)
    while index:
        index -= 1
        new_strings.append(nam[index])

print new_strings
x = new_strings.insert(5,' ')
z = ('').join(new_strings)
print z

'''

# reverse a word
'''
def reverse_a_string_more_slowly(a_string):
    new_strings = []
    index = len(a_string)
    while index:
        index -= 1                       
        new_strings.append(a_string[index])
    return ''.join(new_strings)
'''


# Longest Uncommon Subsequence I
'''


string1 = 'ababa'
string2 = 'cdcba'

x = list(string1)
y = list(string2)
z = len(x)
w = len(y)
count = 0

for i in range(0,z,1):

    if x[i] != y[i]:
        count = count + 1
        i = i +1  
    else:
        break

print count

'''



# detect Capital
'''
x = raw_input('Enter the string')

if x.isupper():
    print 'true'
else:
    print 'false'
'''



#Rotated Digits
'''
class Solution(object):
    def rotatedDigits(self, N):
        counts = 0
        for num in range(1, N+1):
            number = str(num)
            if '3' in number or '7' in number or '4' in number: # This will be an invalid number upon rotation
                continue # Skip this number and go to next iteration
            if '2' in number or '5' in number or '6' in number or '9' in number:
                counts += 1
        return counts
'''


#************************************************************

# DICTIONARY exercise from W3 resources. 


#Write a Python program to count the number of characters (character frequency) in a string. Go to the editor 
#Sample String : google.com'
#Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
'''

string = 'www.google.com'
dictionary = {}

for x in string:

    keys = dictionary.keys()

    if x in keys:
        dictionary[x] += 1
    else:
        dictionary[x] = 1 

print dictionary

'''

#Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string

'''
def string(x):

    new_list_of_string = []
    n = len(x)

    if len()

    new_list_of_string.append(x[0:2])
    new_list_of_string.append(x[-2:])
    z = ''.join(new_list_of_string)

    return z

print string('w3resource')

'''

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


#online test regex

# (([a-zA-Z]{6}[\d]{3}[a-zA-Z\d]+)+[\s]+[a-zA-Z]+([\d])+[\s\d]+[BR,]*[\s]*[a-zA-Z]{0,2}([\d\/]+))





'''

x = raw_input('Enter the strings:')
y = x.split(',')

#sorted_list = []

for items in y:

    z = items.sort()
    sorted_list.append(z)

print sorted_list
'''

################################ Hacker rank regex ########
'''
import re

x = 'rabcdeefgyYhFjkIoomnpOeorteeeeet'
y = re.findall('[b-df-hj-np-tv-z]{1,}([aeiouAEIOU]{2,})[b-df-hj-np-tv-z]{1,}',x)


print y

#for match in y:
 #   print match

'''
######################################################## 
# string w3 resources 

'''
x = 'www.google.com'
dictionary = {}

for letters in x:

    keys = dictionary.keys()

    if letters in keys:
        dictionary[letters] += 1
    else:
        dictionary[letters] = 1 

print dictionary

'''


#Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself. Go to the editor 
#Sample String : 'restart'
#Expected Result : 'resta$t'

'''
x = 'restart'

char = x[0]
y = len(x)

new = x.replace(char, '$')
new = char + new


'''
'''
words_list = ['jhadfkd','nflafl','anfnanflnaf']
word_len = []
for n in words_list:
    word_len.append((len(n), n))
    print word_len
    #word_len.sort()
    #return word_len[-1][1]

#print(find_longest_word(["PHP", "Exercises", "Backend"]))

'''



#x = '([a-zA-Z]{6}[\d]{3}[a-zA-Z\d]+)+[\s]+[a-zA-Z]+([\d])+[\s\d]+[BR,]*[\s]*[a-zA-Z]{0,2}([\d\/]+)'



#10. Write a Python program for counting sort. 
'''
import re
x = "According to Wikipedia In computer science, counting sort is an algorithm for sorting a collection of objects according to keys that are small integers; that is, it is an integer sorting algorithm. It operates by counting the number of objects that have each distinct key value, and using arithmetic on those counts to determine the positions of each key value in the output sequence. Its running time is linear in the number of items and the difference between the maximum and minimum key values, so it is only suitable for direct use in situations where the variation in keys is not significantly greater than the number of items. However, it is often used as a subroutine in another sorting algorithm, radix sort, that can handle larger keys more efficiently"

pattern = 'sort'

match = re.findall(pattern, x)
#print match
total_num = len(match)
print total_num

'''

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# list excersice from w3resources

#71. Write a Python program to check if all dictionaries in a list are empty or not. Go to the editor
#Sample list : [{},{},{}]
#Return value : True
#Sample list : [{1,2},{},{}]
#Return value : False3
'''
x = [{1:2},{}]

for i in x:
    print i 

'''
'''
x = [{1:2},{},{}]

for i in x:

    if len(i) == 0:
        print 'list is emppty'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    else:
        print 'list is not emplty'


'''

#70 70. Write a Python program to get the depth of a dictionary

'''
def dict_depth(d):
    if isinstance(d, dict):
        return 1 + (max(map(dict_depth, d.values())) if d else 0)
    return 0
dic = {'a':1, 'b': {'c': {'d': {}}}}
print(dict_depth(dic))


'''

#69

#Write a Python program to remove duplicates from a list of lists.
'''
x = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
count = 0

for i in x:

    count += 1 
    
    if count > 1:
        del[i]

print x
print y 

'''
'''
#dup Linux coursework 

count = 0 
i = 0
A = [1,3,9,8,8,9,4,9,9,1]
while i in range(0,len(A)):
	B = set(A)
	A1 = A[i]
	bb = A[i]
	A.remove(bb)
	if bb in B:
		count = count + 1
		A.remove(bb)
	i = i + 1
print (count)

'''

'''
even = False

if even = True:
	print("It is even!")
'''

x = 5
y = 10
z = x + y
print z







