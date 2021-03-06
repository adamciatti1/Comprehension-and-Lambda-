''' 1)
Write a Python program to filter a list of integers using Lambda. Go to the editor
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
'''
from distutils.log import error
import os
from re import X
clear = lambda: os.system("cls") 
clear()

original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_list = list(filter(lambda num: num % 2 == 0, original_list))
print(even_list)
odd_list = list(filter(lambda num: num % 2 == 1, original_list))
print(odd_list)

''' 2)
find which days of the week have exactly 6 characters.
'''

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

new_list = list(filter(lambda n: (len(n) == 6), weekdays))
print(new_list)

''' 3)
remove specific words from a given list 
Original list:
['orange', 'red', 'green', 'blue', 'white', 'black']

Remove words:
['orange', 'black']

After removing the specified words from the said list:
['red', 'green', 'blue', 'white']

'''

original_list = ['orange', 'red', 'green', 'blue', 'white', 'black']
 
new_list = list(filter(lambda n: n != 'orange' and n != 'black', original_list))
print(new_list)

''' 4)
 remove all elements from a given list present in another list
Original lists:
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]

Remove all elements from 'list1' present in 'list2:
[1, 3, 5, 7, 9, 10]
 '''
list1 =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]

new_list = list(filter(lambda n: n not in list2, list1))
print(new_list)

''' 5)
find the elements of a given list of strings that contain specific substring using lambda
Original list:
['red', 'black', 'white', 'green', 'orange']
Substring to search:
ack
Elements of the said list that contain specific substring:
['black']
Substring to search:
abc
Elements of the said list that contain specific substring:
[]

'''
original_list = ['red', 'black', 'white', 'green', 'orange']

new_list = list(filter(lambda n: 'ack' in n , original_list))
print(new_list)
newer_list = list(filter(lambda n: 'abc' in n, original_list))
print(newer_list)

''' 6)
check whether a given string contains a capital letter, a lower case letter, a number and a minimum length of 8 characters.
(This is like a password verification function, HINT: Python function 'any' may be useful)
'''

password = input('Enter a password:')

rule1 = lambda x: [y for y in x if y.isupper()]
rule2 = lambda x: [y for y in x if y.islower()]
rule3 = lambda x: [y for y in x if y.isdigit()]

if len(rule1(password)) != 0 and len(rule2(password)) != 0 and len(rule3(password)) != 0 and len(password) >= 8:
    print('valid password.')
else:
    print('invalid password.')

''' 7)
Write a Python program to sort a list of tuples using Lambda.

# Original list of tuples:
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Expected Result:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
'''

original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

new_list = sorted(original_scores, key = lambda x: x[1])
print(new_list)