n = int(input("Pattern lines: "))

def square_pattern(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()
            
# square_pattern(n)

def right_angle_pattern(n):
    for i in range(1, n+1):
        for j in range(i):
            print("*", end=" ")
        print()

# right_angle_pattern(n);

def row_numbered_right_angle_pattern(n):
    for i in range(1,n+1):
        for j in range(i):
            print(j+1, end=" ")
        print()

# row_numbered_right_angle_pattern(n)

def col_numbered_right_angle_pattern(n):
    for i in range(1, n+1):
        for j in range(i):
            print(i, end=" ")
        print()
    
# col_numbered_right_angle_pattern(n)

def reverse_right_angle_pattern(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()
        
    for i in range(1, n+1):
        for j in range(n-i+1):
            print("*", end=" ")
        print()

# reverse_right_angle_pattern(n);

def numbered_reverse_angle_pattern(n):
    for i in range(1, n+1):
        for j in range(1,n-i+2):
            print(j, end=" ")
        print()
        
# numbered_reverse_angle_pattern(n)

def pyramid(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ", end=" ")
        
        for j in range(2*i+1):
            print("*", end=" ")
        
        for j in range(n-i-1):
            print(" ", end=" ")
        print()
        
# pyramid(n)

def reverse_pyramid(n):
    for i in range(n):
        for j in range(i):
            print(" ", end=" ")
        
        for j in range(2 * n - (2 * i + 1)):
            print("*", end=" ")
        
        for j in range(i):
            print(" ", end=" ")
        
        print()
        
# reverse_pyramid(n)

def rhombus(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ", end=" ")
        
        for j in range(2 * i + 1):
            print("*", end=" ")

        for j in range(n-i-1):
            print(" ", end=" ")
            
        print()
        
    for i in range(n):
        for j in range(i):
            print(" ", end=" ")
        
        for j in range(2 * n - (2 * i + 1)):
            print("*", end=" ")
        
        for j in range(i):
            print(" ", end=" ")
        
        print()

# rhombus(n)

def half_rhombus(n):
    for i in range(1,n+1):
        for j in range(i):
            print("*",end=" ")
        print()
        
    for i in range(n-1):
        for j in range(n-i-1):
            print("*", end=" ")
        print()
        
    for i in range(1, 2 * n + 1):
        if i <= n:
            star = i
        else:
            star = 2*n-i
            
        print("* " * star)
        
# half_rhombus(n)

def ones_zeros_right_angle_pattern(n):
    for i in range(n):
        if i % 2 == 0:
            num = 0
        else:
            num = 1
        for j in range(i+1):
            print(num, end=" ")
            num = 1 - num;
        print()
        
# ones_zeros_right_angle_pattern(n)

def valley_pattern(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j, end=" ");
        
        for j in range(2 * n - (2 * i)):
            print(" ", end=" ")
            
        for j in range(i, 0, -1):
            print(j, end=" ")
        
        print()
        
# valley_pattern(n)

def number_sequence_right_angle(n):
    sum = 1;
    for i in range(1,n+1):
        for j in range(i):
            print(sum, end=" ")
            sum += 1
        print()
            
# number_sequence_right_angle(n)

def alphabatical_right_angle_pattern(n):
    for i in range(n):
        for j in range(i+1):
            print(chr(65 + j), end=" ")
        print()
        
# alphabatical_right_angle_pattern(n)

def reverse_alphabatical_right_angle_pattern(n):
    for i in range(n):
        for j in range(n-i):
            print(chr(65 + j), end=" ")
        print()
        
# reverse_alphabatical_right_angle_pattern(n)

def row_vice_alphabatical_right_pattern(n):
    for i in range(n):
        for j in range(i+1):
            print(chr(65 + i), end=" ")
        print()

# row_vice_alphabatical_right_pattern(n)

def letter_pyramid(n):
    
    for i in range(n):
        for j in range(n-i):
            print(" ", end=" ")
        
        ch = ord('A')
        breakpoint = 2*i-1 // 2
        for j in range(i+1):
            print(chr(65+j), end=" ")
        
        
        for j in range(i, 0, -1):
            print(chr(65+j-1), end=" ")
        print()
    
# letter_pyramid(n)

def reverse_letter_pyramid(n):
    for i in range(n):
        for j in range(ord('A') + n - 1 - i, ord('A') + n):
            print(chr(j), end=" ")
        print()
        
# reverse_letter_pyramid(n)

def square_hollow_rhombus(n):
    for i in range(n):
        for j in range(n, i, -1):
            print("*", end=" ")
        
        for j in range(2*i):
            print(" ", end=" ")
        
        for j in range(n, i, -1):
            print("*", end=" ")
        print()
    
    for i in range(1,n+1):
        for j in range(i):
            print("*", end=" ")
        
        for j in range(2 * n - (2 * i)):
            print(" ", end=" ")
        
        for j in range(i):
            print("*", end=" ")
        print()
        
# square_hollow_rhombus(n)

def upside_down_valley_pattern(n):
    for i in range(1,n+1):
        for j in range(i):
            print("*", end=" ")
            
        for j in range(2*n-(2*i)):
            print(" ", end=" ")
        
        for j in range(i):
            print("*", end=" ")
        print()
        
    for i in range(1,n+1):
        for j in range(n-i):
            print("*", end=" ")
        
        for j in range(2*i):
            print(" ", end=" ")
        
        for j in range(n-i):
            print("*", end=" ")
        print()

        
        
# upside_down_valley_pattern(n)

def hallow_effect_pattern(n):
    for i in range(n):
        for j in range(n):
            if(i == 0 or i == n-1 or j == 0 or j == n-1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

# hallow_effect_pattern(n)

def numbered_inward_square(n):
    for i in range(2*n-1):
        for j in range(2*n-1):
            top = i
            left = j
            right = (2*n-2) - j
            bottom = (2*n-2) - i
            
            minDist = min(top, left, right, bottom)
            
            print(n - minDist, end=" ")
        print()
        
# numbered_inward_square(n)

def pattern_F():
    for i in range(5):
        if i == 0 or i == 2: 
            for j in range(5):
                print("x", end="")
        else:
            print("xx", end="")
        print()