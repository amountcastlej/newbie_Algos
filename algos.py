##Create a function sum() that returns the sum of the two numbers passed as it's arguments: Ex sum(2,5) should return 7

def sum(num1, num2):
    return num1+num2

##Log positive numbers starting at 2019, counting down by 8

def CountDownBy8():
	for i in range(2019, 0, -8):
		print(i)


##Kelvin wants to convert between temperature scales. Create celcius to Fahrenheit(cDegrees) that accepts a number of degrees in Celcius, and returns the equivalent temperature as expressed in Fahrenheit degrees. For review, Fahrenheit = (9/5 * Celcius) + 32

def celciusToFahrenheit(cDegrees):
	return (9/5 * cDegrees + 32)

##Given an array, write a function that changes all positive numbers in the array to "big"

def makeItBig(arr):
	for i in range(0, len(arr)):
		if arr[i] > 0:
			print(arr[i])
			arr[i] = "big"
	return arr


##Write a loop that makes seven calls to console.log to output the following triangle:

#
##
###
####
#####
######
#######


num = '#'
for i in range(1, 8, 1):
    print(num)
    num = num + '#'

#String Times
#Given a string & a non-negative int n, return a larger string that is is n copies of the original string
def string_times(str, n):
	return str * n
	result = ""
	for i in range(n):
		result += str
	return result
string_times('Hi', 2)
string_times('Hi', 3)
string_times('Hi', 1)

#Front Times
#Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front
def front_times(str, n):return str[:3] * n
	front_len = 3
	for i in range(n):
		result = result + front
	return result
front_times('Chocolate', 2)
front_times('Chocolate', 3)
front_times('Abc', 3)

#String Bits
#Given a string, return a new string made of every other char starting with the first, so "hello" yields "hlo"
def string_bits(str):return str[::2] => [start:stop:step]
	result = ""
	for i in range(len(str)):
		if i % 2 == 0:result = result + str[i]
	return result
string_bits('Hello')
string_bits('Hi')
string_bits('Heeololeo')

#Missing CharGiven a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string
def missing_char(str, n):
	front = str[:n]
	back = str[n+1:]  
	return front + back
missing_char('kitten', 1)
missing_char('kitten', 0)
missing_char('kitten', 4)

#String Times
#Given a string & a non-negative int n, return a larger string that is is n copies of the original string
def string_times(str, n):
	return str * n
	result = ""
	for i in range(n):
		result += str
	return result
string_times('Hi', 2)
string_times('Hi', 3)
string_times('Hi', 1)

#Front BackGiven a string, return a new string where the first and last chars have been exchanged.
def front_back(str):
	if len(str) <= 1:
		return str
	mid = str[1:len(str)-1]
	return str[len(str)-1] + mid + str[0]
front_back('code')

#array_count9
#Given an array of ints, return the number of 9's in the array.
def array_count9(nums):
	nines = 0
	for i in range(len(nums)):
		if nums[i] == 9:
			nines += 1
	return nines
array_count9([1, 2, 9])
array_count9([1, 9, 9])
array_count9([1, 9, 9, 3, 9])

#Array front9
#Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4

def array_front9(nums):
	end = len(nums)
	if end > 4:
		end = 4
	for i in range(end):
		if nums[i] == 9:
    			return True
	return False
array_front9([1, 2, 9, 3, 4])
array_front9([1, 2, 3, 4, 9])
array_front9([1, 2, 3, 4, 5])

#Array123
#Given an array of ints, return True if the sequence of numbers 1,2,3 appears in the array somewhere
def array123(nums):
	for i in range(len(nums)-2):
    	if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
		return True
	return False
array123([1, 1, 2, 3, 1]) 
array123([1, 1, 2, 4, 1])
array123([1, 1, 2, 1, 2, 3])

#First Half
#Given a string of even length, return the first half.
def first_half(str):
	half = len(str)
return (str[0:half/2])
first_half('WooHoo')
first_half('HelloThere')

#First Two
#Given a string, return the string made of it's first two chars, so the string "Hello" yields "He".
def first_two(str):
	return str[:2]
first_two('Hello')
first_two('abcdefg')
first_two('ab')

#Without End
#Given a string, return a verison without the first and last character
def without_end(str):
	return str[1:-1]
without_end('Hello')
without_end('java')
without_end('coding')

#Combo String
#Given 2 strings, a and b, return a string of the form short + long + short, with the shorter string on the outside and the longer string on the inside
def combo_string(a, b):
	if len(a) < len(b):
		return a + b + a
	if len(b) < len(a):
		return b + a + b
combo_string('Hello', 'hi')
combo_string('hi', 'Hello')
combo_string('aaa', 'b')

#Non Start
#Given 2 strings, return their concatenation, except omit the first char of each
def non_start(a, b):
	return a[1:] + b[1:]
non_start('Hello', 'There')
non_start('java', 'code')
non_start('shotl', 'java')

#Left2
#Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end
def left2(str):
	first2 = str[:2]
	return str[2:] + first2
left2('Hello')
left2('java')
left2('Hi')

#First Last 6
#Given an array of ints, return True if 6 appears as either the first or last element in the array
def first_last6(nums):
	return (nums[0]==6 or nums[-1] == 6)
first_last6([1, 2, 6])
first_last6([6, 1, 2, 3])
first_last6([13, 6, 1, 2, 3])

#Same First & last
#Given an array of ints, return True if the array is length 1 or more, and the first element and last element are equal
def same_first_last(nums):
	return len(nums) > 0 and nums[0] == nums[-1]
same_first_last([1, 2, 3])
same_first_last([1, 2, 3, 1])
same_first_last([1, 2, 1])

#Common End
#Give 2 arrays of ints, a and b, return True if they ahve the same first element or they have the same last element. Both arrays will be length 1 or more
def common_end(a, b):
	return a[0] == b[0] or a[-1] == b[-1]
common_end([1, 2, 3], [7, 3]
common_end([1, 2, 3], [7, 3, 2]
common_end([1, 2, 3], [1, 3]

#Sum3
#Given an array of ints length 3, return the sum of all the elements
def sum3(nums):
	return nums[0] + nums[1] + nums[-1]
sum3([1, 2, 3])
sum3([5, 11, 2])
sum3([7, 0, 0])

#Rotate Left 3
#Given an array of ints length 3, return an array with the elements "rotated left"
def rotate_left3(nums):
	return nums[1:] + nums[:1]
rotate_left([1, 2, 3])
rotate_left([5, 11, 9])
rotate_left([7, 0, 0])

#Reverse3
#Given an array of ints length 3, return a new array with the elements in reverse order
def reverse3(nums):
	return nums[::-1]
	return reverse3(nums[1:]) + nums[:1] if nums else nums
reverse3([1, 2, 3]) 
reverse3([5, 11, 9]) 
reverse3([7, 0, 0]) 
