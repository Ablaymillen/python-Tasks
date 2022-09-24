# Create a function with name "localMaxMin" that pass as argument a list
# and returns the indexes of all local minima and local maxima
def localMaxMin(arr):
    # length of an array
    n = len(arr)
    # arrays to store local max and min indexes
    loc_max = []
    loc_min = []

    # Checking first elements of an array
    if arr[0] > arr[1]:
        loc_max.append(0)
    elif arr[0] < arr[1]:
        loc_min.append(0)

    # process of finding local min and max indexes through for loop
    for i in range(1, n - 1):
        # loc max
        if arr[i - 1] < arr[i] > arr[i + 1]:
            loc_max.append(i)
        # loc min
        elif arr[i - 1] > arr[i] < arr[i + 1]:
            loc_min.append(i)

    # Checking last elements of an array
    if arr[-1] > arr[-2]:
        loc_max.append(n - 1)
    elif arr[-1] < arr[-2]:
        loc_min.append(n - 1)

    print_loc_max(loc_max)
    print_loc_min(loc_min)


# Print loc maxima elements
def print_loc_max(loc_max):
    if len(loc_max) == 0:
        print("There are no points of Local maxima.")
    else:
        maxes = ''
        for num in loc_max:
            maxes += str(num) + ' '
        print(f'Points of Local maxima"" are : {maxes}')


def print_loc_min(loc_min):
    if len(loc_min) == 0:
        print("There are no points of Local minima.")
    else:
        mins = ''
        for num in loc_min:
            mins += str(num) + ' '
        print(f'Points of Local maxima"" are : {mins}')


localMaxMin([10, 20, 15, 14, 13, 25, 5, 4, 3])


# Write a function "longSubArray" that pass as an argument a list. The problem is to
# find the length of the longest contiguous subarray such that every element in the
# subarray is strictly greater than its previous element in the same subarray.
def longSubArray(arr):
    max_length = 1
    count = 1
    if len(arr) == 0:
        return 0

    for i in range(1, len(arr)):
        if arr[i - 1] < arr[i]:
            count = count + 1
        else:
            if count > max_length:
                max_length = count
            count = 1
    if max_length < count:
        max_length = count
    return max_length


print(longSubArray([5, 6, 3, 5, 7, 8, 9, 1, 2]))


# Write a function "indexF" that pass as ana rgument a string. If the letter f occurs only once in this
# string, print its index. If it occurs two or more times, output the index of its first and last
# occurrence. If the letter f does not occur in the given line, do not print anything. You cannot use
# the 'count' method and 'loops' when solving this problem.
def indexF():
    s = str(input("input: \n"))

    if s.count("f") >= 2:
        print("output: \n", s.find("f"), s.rfind("f"))
    elif s.find("f") == 0:
        print("output: \n", s.find("f"))
    else:
        print("output: \n", s.find("f"))


# Write a recursive function sum(a, b) that returns the sum of a and b. only +1 and -1
# arithmetic operations allowed. Do not use loops
def sum(a, b):
    if a == 0:
        return b
    else:
        return sum(a - 1, b + 1)


print(sum(1, 4))


# Given a natural number n≤9, output a ladder of n steps, the i-th step consists of numbers
# from 1 to i without spaces.
def ladder(n):
    if n <= 9:
        for x in range(1, n + 1):
            s = ''
            for i in range(1, x + 1):
                s += str(i)
            print(s)


ladder(5)


# create a function sumFact(a) that passes an argument a natural number, and calculate the sum
# of 1!+2!+3!+...+n!. You can use only one loop.
def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


def sumFact(n):
    summ = 0
    for i in range(1, n + 1):
        summ += factorial(i)
    return summ


print(sumFact(3))


# Write a function lastMaxIndex(lst) that passes as an argument a list, and returns the maximum
# element and it's index. If there is multiple maximum elements, return the last index.
def lastMaxIndex(arr):
    max = arr[0]
    index = 0
    for i in range(1, len(arr)):
        if arr[i] >= max:
            max = arr[i]
            index = i
    return [max, index]


print(*lastMaxIndex([1, 2, 3, 2, 5, 3, 1]))


# Given a list of numbers, determine and print the number of elements that are greater than both of
# their neighbors.
def greater_than_neighbors():
    # list comprehension
    arr = [int(s) for s in input().split()]
    count = 0
    for i in range(1, len(arr) - 1):
        if arr[i - 1] < arr[i] > arr[i + 1]:
            count += 1
    print(count)


# Given a list of numbers, find the closest element in array to given number.
# If there is multiple closest, print any of them
def closest_element():
    # list comprehension
    arr = [int(s) for s in input().split()]
    n = int(input())
    min_sub = abs(n - arr[0])
    index = 0
    for i in range(1, len(arr)):
        if abs(n - arr[i]) < min_sub:
            min_sub = abs(n - arr[i])
            index = i
    print(arr[index])


def ranking_of_heights(heights, aidos):
    heights.sort(reverse=True)
    for i in range(0, len(heights)):
        if aidos > heights[i]:
            print(i + 1)
            break


# 163 165 154 160 155 157 157 160 input
# 162

# Find in this list two numbers whose product is maximal. Print these numbers in non-decreasing order.
# The solution should have O(n) complexity, where n is the size of the list. That is, sorting cannot be used.
def max_product(lst):
    n = len(lst)
    a, b, ma, mb = 0, 0, 0, 0
    for i in range(0, n):
        if lst[i] > a:
            b = a
            a = lst[i]
        elif lst[i] > b:
            b = lst[i]
        # negative values
        if lst[i] < 0 and (abs(lst[i]) > abs(ma)):
            mb = ma
            ma = lst[i]
        elif lst[i] < 0 and (abs(lst[i]) > abs(mb)):
            mb = lst[i]
    if mb * ma > a * b:
        print(ma, mb)
    else:
        print(a, b)


# It is required to “compress” it by moving all non-zero elements to the left side of the list
# without changing their order, and all zeros to the right side.
def compress_zeros(a):
    a.sort(key=lambda v: v == 0)
    print(a)


compress_zeros([4, 0, 5, 0, 3, 0, 0, 5])


# Several people took part in the Olympiad in Informatics.Determine and display the average scores of the
# participants in the Olympiad in the 9th grade, in the 10th grade, in the 11th grade.
def avg_mark(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum / len(arr)


def olympiad_marks(a):
    # dictionary of a type grade: mark
    olympiad = {}
    for elem in a:
        grade, mark = elem.split()[2:]
        # if grade already exists
        if grade in olympiad:
            olympiad[grade].append(int(mark))
        else:
            # if grade does not exist add one into dict
            olympiad[grade] = [int(mark)]

    for i in range(9, 12):
        print(avg_mark(olympiad[str(i)]), end=' ')
    print('')


olympiad_marks(["Иванов Сергей 9 90", "Сергеев Петр 10 91", "Петров Василий 11 92", "Васильев Иван 9 93"])


# Given a list with sentence, Determine how many different words are in this sentences.

def words_count(a):
    words = []
    for sentence in a:
        for word in sentence.split():
            words.append(word)
    unique_words = set(words)
    print(len(unique_words))


a = ['She sells sea shells on the sea shore;', 'The shells that she sells are sea shells I\'m sure.',
     'So if she sells sea shells on the sea shore,',
     'I\'m sure that the shells are sea shore shells.']

words_count(a)

# A list of countries and cities of each country is given. Then the names of the cities are given.
# For each city, indicate which country it is in. solve this with dictionaires.
a = ["Russia Moscow Petersburg Novgorod Kaluga", "Ukraine Kiev Donetsk Odessa"]
b = ["Odessa", "Moscow", "Novgorod"]


def determine_country(a, b):
    countries = {}
    for elem in a:
        country, *cities = elem.split()
        countries.update({country: cities})

    for city in b:
        for country, cities in countries.items():
            if city in cities:
                print(country)


a = ["Russia Moscow Petersburg Novgorod Kaluga", "Ukraine Kiev Donetsk Odessa"]
b = ["Odessa", "Moscow", "Novgorod"]

determine_country(a,b)


# Given a list, that each element is a pair of synonyms. Please print the output The program should
# output a synonym for the given word.
def find_synonym(a,b):
    dic = {}
    for elem in a:
        words = elem.split()
        dic.update({words[0]: words[1]})
    if b in dic.keys():
        print(dic[b])
    elif b in dic.values():
        print(list(dic.keys())[list(dic.values()).index(b)])


a = ["Hello Hi", "Bye Goodbye", "List Array"]
b = "Hello"
find_synonym(a,b)

a = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4]
print(min([i for i in a if i % 2 != 0]))