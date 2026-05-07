# n = int(input("Enter a number:"))

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

def printing_numbers_from_n(i,n):
    if i > n:
        return
    
    printing_numbers_from_n(i+1,n)
    print(i)

# printing_numbers_from_n(1,n)

        