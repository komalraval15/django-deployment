#problem 1
# Given the string:
s = 'django'

# Use indexing to print out the following:
# 'd'
s[0]
# 'o'
s[-1]
# 'djan'
s[:4]
# 'jan'
s[1:4]
# 'go'
s[4:]
# Bonus: Use indexing to reverse the string
s[::-1]


#problem 2 
# Given this nested list:
l = [3,7,[1,4,'hello']]
# Reassign "hello" to be "goodbye"
l[2][2] = "goodbye"

#problem 3
d1 = {'simple_key':'hello'}

d1['simple_key']

d2 = {'k1':{'k2':'hello'}}

d2['k1']['k2']

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}

d3['k1'][0]['nest_key'][1][0]

#problem 4
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
set(mylist)

#problem 5
age = 4
name = "Sammy"


"Hello my dog's name is Sammy and he is 4 years old"

print("Hello my dog's name is {} and he is {} years old".format(age,name))
