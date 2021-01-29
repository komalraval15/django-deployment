# problem 1


def arrayCheck(nums):
    for i in range(len(nums)-2):
        # Check in sets of 3 if we have 1,2,3 in a row
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
    return False
print(arrayCheck([2,5,9,6]))

# problem 2

def stringBits(str):
    result = ""
    for i in range(len(str)):
        if i % 2 == 0:
            result = result + str[i]
    return result
print(stringBits("komal"))

#problem 3

def end_other(a, b):
  a = a.lower()
  b = b.lower()
  #return (b.endswith(a) or a.endswith(b))
  return a[-(len(b)):] == b or a == b[-(len(a)):]
print(end_other('abc','dfabc'))

#problem 4
def doubleChar(str):
  result = ''
  for char in str:
    result += char * 2
  return result
print(doubleChar("kkr"))

#problem 5
def no_teen_sum(a, b, c):
  return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(n):
    if n in [13, 14, 17, 18, 19]:
        return 0
    return n
print(no_teen_sum(1,13,2))

#problem 6
def count_evens(nums):
  count = 0
  for element in nums:
    if element % 2 == 0:
      count += 1
  return count
print(count_evens([2,4,5,3]))
