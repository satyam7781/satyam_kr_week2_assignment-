'''Write a script that counts the frequency of words
in a given text and stores the result in a
dictionary.'''


#creating Funcyion for Frequency Count
def frequency_count(test_string):
#creating Empty string
    l=[]
#Changing String to List
    l=test_string.split()
#Use loop to count frequency
    wordfreq=[l.count(p) for p in l]
#printing result
    print(dict(zip(l,wordfreq)))
#giving input
test_string=input("enter a string \n")
#calling Function
frequency_count(test_string)
