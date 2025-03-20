#1. write a  function to reverse a string
def reverse_string(s):
    return s[::-1]
print(reverse_string('hello')) #o/p= 'olleh'

#2.Count the number of vowels in a given string
def count_vowels(s):
    vowels= 'aeiouAEIOU'
    return sum(1 for ch in s if ch in vowels)
print(count_vowels('ELephant'))  #o/p= 3

#3. Find the fatorial of a given number using recrussion
def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
print(factorial(5))     #o/p= 120

#4. check if given number is prime 
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
print(is_prime(7))  # Output: True

#5. Finf the most frequent Element in list
from collections import Counter
def most_frequent(lst):
    return Counter(lst).most_common(1)[0][0]
print(most_frequent([1, 2, 2, 3, 1, 2]))  # Output: 2

#6. Remove all the duplicates from a list  while maintaing order
def remove_duplicates(lst):
   seen =set()
   result=[]
   for item in lst:
       if item not in seen:
           result.append(item)
           seen.add(item)
   return result
print(remove_duplicates([1,2,2,3,4,1])) # o/p [1,2,3,4]

#7. convert a given int to binary format
def int_to_binary(n):
    return bin(n)[2:]
print(int_to_binary(10))  # Output: '1010'

#8.find the second largest-number in a list
def second_largest(lst):
    unique = list(set(lst))
    unique.sort()
    return unique[-2]
print(second_largest([10, 20, 4, 45, 99]))  # Output: 45

#9. find the sum of two digits of a given number
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))
print(sum_of_digits(123))  # Output: 6

#10. find the longest word in a given sentence
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)
print(longest_word("Python is amazing"))  # Output: 'amazing'

#11. merge two sorted lists into one sorted list
def merge_sorted_lists(a, b):
    return sorted(a + b)
print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  # Output: [1, 2, 3, 4, 5, 6]

#12. check if two strings are anagrams of each other
def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)
print(are_anagrams("listen", "silent"))  # Output: True

#13. count the occurence of each word in a sentence
from collections import Counter
def word_count(sentence):
    words = sentence.split()
    return dict(Counter(words))
print(word_count("this is a test this is"))  
# Output: {'this': 2, 'is': 2, 'a': 1, 'test': 1}

#14. generate a fibonnacci  sequence up to n terms
def fibonacci(n):
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]
print(fibonacci(7))  # Output: [0, 1, 1, 2, 3, 5, 8]

#15. convert a list of strings to uppercase
def to_uppercase(lst):
    return [s.upper() for s in lst]
print(to_uppercase(['anisha', 'python']))  # Output: ['ANISHA', 'PYTHON']

#16. find thw  intersections  of two lists
def list_intersection(a, b):
    return list(set(a) & set(b))
print(list_intersection([1, 2, 3], [2, 3, 4]))  # Output: [2, 3]

#17. remove punctuation from a given string
import string
def remove_punctuation(s):
    return s.translate(str.maketrans('', '', string.punctuation))
print(remove_punctuation("Hello, Anisha! How are you?"))  
# Output: 'Hello Anisha How are you'

#18. flatenned a nested list into a single list
def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]
print(flatten_list([[1, 2], [3, 4], [5]]))  # Output: [1, 2, 3, 4, 5]

#19. convet a given list into a dict with indices as keys
def list_to_dict(lst):
    return {i: lst[i] for i in range(len(lst))}
print(list_to_dict(['a', 'b', 'c']))  
# Output: {0: 'a', 1: 'b', 2: 'c'}

#20. check if a given string string is a palindrome
def palindrome(s):
    return s[::-1]
print(palindrome('madam'))  # o/p= madam
