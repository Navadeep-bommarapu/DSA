from math import *
# n = int(input("Enter a number:"))


def count_digits(n):
    # count = int(log10(n) + 1)
    
    count = 0
    while n != 0:
        count += 1
        n = n // 10
    print(count)

# count_digits(n)

def reverse_number(n):
    rem = 0
    while n != 0:
        digit = n % 10
        n = n // 10
        rem = (rem * 10) + digit
    print(rem)
    
# reverse_number(n)

def is_palindrome(n):
    dup = n
    if n < 0 or (n % 10 == 0 and n != 0):
        return False

    rem = 0
    while n > 0:
        rem = rem * 10 + n % 10
        n //= 10
    return rem == dup

# result = is_palindrome(n)
# print(result)

def armstrong_num(n):
    dup = n
    string = str(n)
    
    sum = 0
    digit = len(string)
    print(digit)
    
    while n > 0:
        digit_no = n % 10
        cube_digit = digit_no ** digit
        sum += cube_digit
        n //= 10
    print(sum == dup)

# armstrong_num(n)


def divisors(n):
    # for num in range(1,n+1):
    #     if n % num == 0:
    #         print(num, end=" ")
    
    mylist = []
    for num in range(1, int(sqrt(n)+1)):
        if n % num == 0:
            mylist.append(num)
            if num != n // num:
                mylist.append(n // num)
            
    mylist.sort()
    for i in mylist:
        print(i, end=" ")

# divisors(n)

def prime_number(n):
    # if n < 0:
    #     return False
    # count = 0
    # for i in range(1, n+1): # Time complexity is O(n)
    #     if n % i == 0:
    #         count += 1
    # return count == 2
    
    count = 0
    for i in range(1, int(sqrt(n)+1)): # Time complexity is O(sqrt(n))
        if n % i == 0:
            count += 1;
            if n // i != i:
                count += 1
    return count == 2

# result = prime_number(n)
# print(result)

# print(sqrt(n))
# print(int(sqrt(n) + 1))

def gcd(num1, num2):
    # for num in range(1, min(num1, num2)+1):
    #     if num1 % num == 0 and num2 % num == 0:
    #         gcd = num

    # Euclidean algorithm 
    # gcd(a, b) = gcd(a - b, b) if a > b
    # gcd(a, b) = gcd(a % b, b) if a >b
    while num1 > 0 and num2 > 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    if num1 == 0:
        gcd = num2
    else:        
        gcd = num1

    return gcd

result = gcd(10,52)
print(result)

def printIncreasingPower(x):
    # for i in range(1,x+1):
    #     if i**2 > x:
    #         return
    #     print(i**2)
    
    i = 1
    while i < x:
        if i**2 > x:
            return
        print(i**2)
        i += 1
        
printIncreasingPower(n)