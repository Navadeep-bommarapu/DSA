n = int(input("Enter a number:"))

def printing_n_times(n):
    if n == 0:
        return
    print("Hello")
    printing_n_times(n-1)

# printing_n_times(n)

def print_numbers(n):
    # Base case
    if  n < 1:
        return
    
    # printing numbers from current to n
    print(n)
    print_numbers(n - 1) 

    # printing numbers from n to current
    print_numbers(n - 1)
    print(n)

# print_numbers(1, n)


def sum_num(n):    
    if n < 1:
        return 0
    
    return n + sum_num(n-1)

# print(sum_num(n))

def printing_numbers_from_i(i,n):
    if i > n:
        return
    
    printing_numbers_from_i(i+1,n)
    print(i)

# printing_numbers_from_i(1,n)

def factorial(n):
    if n == 1:
        return 1
    
    return n * factorial(n-1)
    

# print(factorial(n))

def reverse_arr(n):
    # understanding the concept of reversing an array
    left = 0
    right = len(n) - 1
    while left < right:
        if left == right:
            return
        temp = n[left]
        n[left] = n[right]
        n[right] = temp
        left += 1
        right -= 1
    return n
# print(reverse_arr(n))


# n = [1,2,3,4,5]
# l = 0
# r = len(n) - 1

def recursive_reverse_arr(l, r, n):
    # brute force 
    if l == r:
        print(n)
        return
    
    temp = n[l]
    n[l] = n[r]
    n[r] = temp
    l += 1
    r -= 1
    recursive_reverse_arr(l, r, n)
    
    # using a single parameter
    # if l == len(n) - l - 1:
    #     print(n)
    #     return
    
    # temp = n[l]
    # n[l] = n[len(n) - l - 1]
    # n[len(n) - l - 1] = temp
    # l += 1
    # recursive_reverse_arr(l,n) 

# recursive_reverse_arr(l, r, n)

# n = input("Enter your string: ")
# l = 0
# r = len(n) - 1

def is_palindrome(n):
    n_list = list(n)
    n_list.reverse()
    
    string = ''
    newString = string.join(n_list)
    

    if newString == n:
        return True
    return False

# print(is_palindrome(n))

# Recursive Approach to check the palindrome of a string
# n = input("Enter a string: ")
def recursive_palindrome(i, str):
    if i >= len(str)/2:
        return True
    
    if str[i] != str[len(str) - i - 1]:
        return False
    
    return recursive_palindrome(i+1, str)
    
# print(recursive_palindrome(0, n))

def fibonacci(n):
    if n <= 1:
        return n
    
    return fibonacci(n-2) + fibonacci(n-1)

# print(fibonacci(n))


# Example of multiple recursion call
def hello(n):
    if n <= 0:
        return
    print("hello")
    hello(n - 1)
    hello(n - 1)
    
# hello(n)


def subsequence(index, n):
    if index >= len(n):
        print(n)
        return
    
    n.append(arr[index])
    subsequence(index+1,n)
    n.remove(arr[index])
    subsequence(index+1,n)

arr = [3,1,2]
subsequence(0,[])

a = [1,2,3,4]
def reverseArray(a):
    # Write your code here
    left = 0
    right = len(a) - 1
    
    while left < right:
        temp = a[left]
        a[left] = a[right]
        a[right] = temp
        left += 1
        right -= 1
        
    return a

print(reverseArray(a))