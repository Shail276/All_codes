#1 1. Write a Python program to sum all the items in a list.
'''
x = [5,4,5,3]

sum = 0

for i in x:
	sum += i

print sum

'''

#2 Write a Python program to multiplies all the items in a list.
'''
x = [5,4,5,3] 

mul = 1

for i in x:

	mul *= i

print mul

'''

#3 Write a Python program to get the largest number from a list.
'''
x = [6,-7,9,10]

max = x[0]

for i in x:

	if i > max:
		max = i

print max

'''

#4 4. Write a Python program to get the smallest number from a list.

'''
x = [6,-7,9,10]

min = x[0]

for i in x:

	if i < min:
		min = i

print min

'''

#5 5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. Go to the editor 
#Sample List : ['abc', 'xyz', 'aba', '1221']
#Expected Result : 2

'''
Sample_List = ['abc', 'xyz', 'aba', '1221']
count = 0

for x in Sample_List:

	if len(x) >= 2 and x[0] == x[-1]:
		count += 1

print count

'''


#6 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. Go to the editor 
#Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

x = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

max = x[0]

for i in x:
	i[1] 












