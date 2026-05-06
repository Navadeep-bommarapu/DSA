from math import *
n = int(input("Enter a number:"))


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

result = is_palindrome(n)
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

divisors(n)