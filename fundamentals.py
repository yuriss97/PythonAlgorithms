# 1)FizzBuzz:
# Write a program that prints the numbers from 1 to 100. For multiples of three, print "Fizz" instead of the number.
# For multiples of five, print "Buzz". For numbers that are multiples of both three and five, print "FizzBuzz".

'''

count = 1

while count<=100:
    if count % 3 == 0 and count % 5 == 0:
        print("FizzBuzz")
    elif count % 3 == 0:
        print("Fizz")
    elif count % 5 == 0:
        print("Buzz")
    else:
        print(count)
    count+=1

'''


# 2)Fibonacci Sequence:
# Write a program that generates the Fibonacci sequence up to a specified number of terms.
# The Fibonacci sequence starts with 0 and 1, and each subsequent term is the sum of the two preceding terms.

'''

def fibonacciSequence(numberOfTerms):
    count=0
    sequenceList = [0,1]    # List with the first two terms

    if numberOfTerms<2:     # Number of terms has to be greater or equal to 2
        print("Please, provide a number greater than 2")
    else:
        while count<numberOfTerms-2:
            a = sequenceList[count]
            b = sequenceList[count+1]
            sequenceList.append(a+b)
            count+=1
    print(sequenceList)

fibonacciSequence(8)        # Call the function with the desired number of terms

'''

# 3)Prime Numbers:
# Write a program that determines whether a given number is prime or not.
# A prime number is a positive integer greater than 1 that has no positive divisors other than 1 and itself.

'''

def isItPrime(n):
    if n <= 1:
        print("Please provide a number grater than 1.")
        return
    
    for i in range(2, n):
        if n % i == 0:
            print("{} is not a prime number.".format(str(n)))
            return

    print("{} is a prime number.".format(str(n)))

isItPrime(7)

'''

# 4)Sorting Algorithms:

# Implement various sorting algorithms such as bubble sort, insertion sort, or merge sort.
# Test the algorithms on different input arrays and compare their performance.

'''

arrayOne = [3, 8, 2, 34, 34, 23, 22]
isSorted = False

while not isSorted:
    isSorted = True
    for i in range(len(arrayOne) - 1):
        if arrayOne[i] > arrayOne[i+1]:
            temp = arrayOne[i]
            arrayOne[i] = arrayOne[i+1]
            arrayOne[i+1] = temp
            isSorted = False
    
print(arrayOne)

'''

# 5)Write a program that accepts a sentence as input and outputs the number of words in the sentence.

'''

sentence = " How many words    does this sentence   has? "

# Split the sentence into words
numberOfWords = sentence.split()

print(len(numberOfWords))

'''

# 6) Create a function that takes a list of integers as input and returns a new list with only the even numbers.

''' 

def returnEvenNumbers(listOfNumbers):
    listOfEvenNumbers = []

    # Looping thru all the elements from 'listOfNumbers'
    for i in listOfNumbers:
        # Checking if the number is even
        if i % 2 == 0:
            # If the number is even, add it to 'listOfEvenNumbers'
            listOfEvenNumbers.append(i)

    return listOfEvenNumbers

listOfNumbers = [3,7,2,23,6,423,67,362,765,264,77]

print(returnEvenNumbers(listOfNumbers))

'''    

# 7) Implement a function that checks if a given string is a palindrome (reads the same forwards and backwards).

'''

def isItPalindorme(word):
    # Lenght of the word
    wordLenght = len(word)

    # Loop variable
    i = 0

    # Loop until middle letter is identified
    while i < wordLenght / 2:
        # Check if the opposite letter is the same
        if word[i] != word[wordLenght - (i+1)]:
            return False
        i += 1
    return True

# Test cases
word = "abcdeedcba"
print(isItPalindorme(word))

word = "abcdedcba"
print(isItPalindorme(word))

word = "abcdeedfcba"
print(isItPalindorme(word))

'''

# 8) Implement a function that counts the frequency of each word in a given text and returns a dictionary with word counts.

'''

def count_word_frequency(text):
    # Creating dictionary
    word_counts = {}
    # Converting text to lower case so the words are not case sensitive and using split to separate each word
    words = text.lower().split()
    
    # Looping thru each word in words array
    for word in words:
        # If word is found in the dictionary, increment its value by one, if not, set value to one
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    return word_counts

text = "This sentence is repeating some words and this sentence is repeating some words"
frequency = count_word_frequency(text)
print(frequency)

'''

# 9) Implement a function that return an address from a dictionary given a specific name

'''

addressDictionary = {'name1':'Boulevard One','name2':'Ealkwood Avenue','name3':'Elton Street'}

def findAddress(name,adressDictionary):
    if name in adressDictionary:
        return adressDictionary[name]
    else:
        return "Name not found"
    
print(findAddress("name1",addressDictionary))
print(findAddress("name2",addressDictionary))
print(findAddress("name4",addressDictionary))

'''
