'''Implement a program that takes a tuple of
integers and returns a new tuple with even
numbers only.'''

#creating function 
def even_num(number):
#using single line args to get only even number as a tuple form given tuple
    even=tuple(i for i in number if i%2==0)
#returning the even number
    return even
#giving numbers as an input       
number=(1,2,3,4,5,6,7,8)
#storint Even number in a tuple
even=even_num(number)
#printing the even number from the given tuple
print("Even numbers are",even)