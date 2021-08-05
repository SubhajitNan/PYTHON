# Python program to print Positive Numbers in a List Using List Comprehension

# list of numbers
list1 = [-10, -21, -4, 45, -66, 93]

# using list comprehension
pos_nos = [num for num in list1 if num >= 0]

print("Positive numbers in the list: ", *pos_nos)
      
******************************************************************
 
# Python program to print positive Numbers in a List Using While Loop

# list of numbers
list1 = [-10, 21, -4, -45, -66, 93]
num = 0

# using while loop	
while(num < len(list1)):
	
	# checking condition
	if list1[num] >= 0:
		print(list1[num], end = " ")
	
	# increment num
	num += 1
      
******************************************************************

# Python program to print positive Numbers in a List Using For Loop

# list of numbers
list1 = [11, -21, 0, 45, 66, -93]

# iterating each number in list
for num in list1:
    if num >= 0:

        # checking condition
        print(num, end = " ")

*******************************************************************
