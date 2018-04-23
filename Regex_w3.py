'''

import re
my_regex_str = "Ethernet Routing Switch 3549GTS-PWR+"
a = re.findall(r"(.{5}).+ (.+?)\s(\d{2,4}).+-(.{4})", my_regex_str)
z=a[0][2]
print z 
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

