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