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
