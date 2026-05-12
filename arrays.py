arr = list(map(int, input("Enter array elements: ").split())) or [0,0,1,2,3,0,9,8,0,2,4,0,1]

# Solutions in the Topic will be solved accordingly
# Brute -> Better -> Optimal

# Largest element in an Array
# Brute Force Approach - Sorting an array and accessing the last index/element
def largest_element(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1,len(arr)):
            if arr[min] > arr[j]:
                min = j
            
        arr[min], arr[i] = arr[i], arr[min]
    
    return arr[len(arr) - 1]

# print(largest_element(arr))

# Optimised Approach - declaring a variable (largest) and initialize to the first element, 
#                      use for loop and iterate through the array, 
#                      compare variable with the elements in the array, 
#                      if the element is larger than the variable then assign the element to the variable


def optimal_largest_element(arr):
    largest = arr[0]
    
    for i in arr:
        if i > largest:
            largest = i
    
    return largest

# print(optimal_largest_element(arr))


# Second Largest Element
# Brute Force Approach - Sorting an array and taking the len of array - 2
def second_largest_element(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[min] > arr[j]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    
    for i in range(len(arr)-2, -1, -1):
        if arr[i] < arr[len(arr)-1]:
            return arr[i]
    

# print("Brute Approach",second_largest_element(arr))

# Better Approach - declaring a (largest and sec_largest) variable and assigning the first element to it, 
#                    and loop in the array and if the elment is larger than the largest variable then assign the element to the largest and 
#                    another for loop,  if the second_largest element is larger than the element 
#                    but smaller than the largest variable thats the second largest element in the array
def better_second_largest_element(arr):
    largest = arr[0]
    second_largest = -1
    
    for i in arr:
        if i > largest:
            largest = i
            
    for i in arr:
        if largest > i and i > second_largest:
            second_largest = i
        
    return second_largest

# print("Better Approach: ",better_second_largest_element(arr))

# Optimal Approach - Assigning two variables (largest, sec_largest) and 
#                    for every element comparing if the element is larger than the variable largest,
#                    then assigning largest to the second largest and element to the largest
# element > largest: 
#       sec_largest = largest  
#       largest = i

# consider in a classroom if a person scores a 50 marks he is the highest, 
# and if the second person announced his marks then he will be the highest and 
# the first person becomes the second largest
def optimal_second_largest_element(arr):
    largest = arr[0]
    second_largest = -1
    for i in arr:
        if i > largest:
            second_largest = largest
            largest = i
        elif i < largest and i > second_largest:
            second_largest = i
    
    return second_largest

# print("Optimal Approach: ",optimal_second_largest_element(arr))

# Check if the array is sorted:
# Brute Approach - Only Solution
def check_arr_sort(arr):
    result = False
    for i in range(len(arr)-1):
        if arr[i] <= arr[i+1]:
            result = True
        else:
            return False
    
    return result

# print(check_arr_sort(arr))


# Removing duplicated from the sorted array
# Brute Approach - converting the array into set of unique elements and converting back to the array
def remove_duplicates(arr):
    
    # arr = set(arr)
    # print(len(arr))
    # arr = list(arr)
    # print(arr, len(arr))
        
    j = 0
    for i in range(len(arr)):
        if arr[i] != arr[j]:
            arr[j+1] = arr[i]
            j += 1
    
    result = []
    for i in range(j+1):
        result.append(arr[i])
    
    return result
    # return arr

# print(remove_duplicates(arr))

# Left Rotate Array - shifting first element to the last index and 
#                     shifting every element to one index less than the original index
# [1,2,3,4,5] ---> [2,3,4,5,1]
# Brute Approach
def left_rotate_arr(arr):
    temp = 0
    
    for i in range(1,len(arr)):
        arr[i], arr[temp] = arr[temp], arr[i]
        temp += 1
    
    # n = len(arr)
    # j = 1
    # while j < n:
    #     arr[j], arr[j-1] = arr[j-1], arr[j]
    #     j+=1
        
    return arr

# print(left_rotate_arr(arr))

# Left Rotate By K - shifting the first k element to the back and 
#                    shifting the rest of the element to the front
# [1,2,3,4,5,6] k=2 ---> [3,4,5,6,1,2]
# Brute Approach
def left_rotate_by_k(arr, k):
    n = len(arr)
    k = (k % n) + 1
    temp = arr[:k]
    print(temp)
    
    for i in range(k,n):
        arr[i-k] = arr[i]
    
    for i in range(n-k, n):
        arr[i] = temp[i-(n-k)]

    return arr
            
# arr = [1,2,3,4,5,6,7]

# print(left_rotate_by_k(arr, 3))

# Optimal Approach
def reversed(arr, i, k):
    while i <= k:
        arr[i], arr[k] = arr[k], arr[i]
        i += 1
        k -= 1
    # print(arr)

def optimal_left_rotate_by_k(arr,k):
    n = len(arr)
    k = k % n
    
    reversed(arr, 0, k-1)
    reversed(arr, k, n-1)
    reversed(arr, 0, n-1)
    return arr

# print(optimal_left_rotate_by_k(arr, 5))

# Move Zero to End of the array
# Brute Force - Traversing the array and pushing the non zero elements into the new array, 
#               and traversing the new array and making the element arrange in the original array of non zeros, 
#               and from the len of temp and the original array len the element will be zeros
# arr=[0,1,5,3,0,2,4] ---> [1,5,3,2,4,0,0]
def move_zero_to_end(arr):
    n = len(arr)
    temp = []
    for i in range(n):
        if arr[i] != 0:
            temp.append(arr[i])

    nz = len(temp)
    for i in range(nz):
        arr[i] = temp[i]
    
    for i in range(nz, n):
        arr[i] = 0
        
    return arr

# print(move_zero_to_end(arr))

# Optimal Approach 
def optimal_move_zero_to_end(arr):                
    i = 0
    j = 0
    for index in range(len(arr)):
        if arr[index] == 0:
            j = index
            i = index + 1
            break
    
    print(arr)
    while i < len(arr):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
        else:
            i += 1
            
        
    return arr

print(optimal_move_zero_to_end(arr))












































































































# def largest_element_practice(arr):
#     # Brute Approach
#     for i in range(len(arr)):
#         min = i
#         for j in range(i+1,len(arr)):
#             if arr[min] > arr[j]:
#                 min = j
#         arr[min], arr[i] = arr[i], arr[min]
    
#     return arr[len(arr) - 1]
        
        
    
#     # Optimal Approach
#     largest = arr[0]
#     for i in range(len(arr)):
#         if arr[i] > largest:
#             largest = arr[i]
        
#     return largest

# print(largest_element_practice(arr))


# def second_largest_element_practice(arr):
#     # Brute Approach
#     # for i in range(len(arr)):
#     #     min = i
#     #     for j in range(i+1,len(arr)):
#     #         if arr[min] > arr[j]:
#     #             min = j
            
#     #     arr[min], arr[j] = arr[j], arr[min]
    
#     # for i in range(len(arr), -1, -1):
#     #     if arr[i] < arr(len(arr) - 1):
#     #         return arr[i]
    
#     # Better Approach
#     # largest = arr[0]
#     # second_largest = -1
#     # for i in arr:
#     #     if i > largest:
#     #         largest = i
        
#     # for i in arr:
#     #     if largest > i and i > second_largest:
#     #         second_largest = i
        
#     # return second_largest

#     # Optimal Approach
#     largest = arr[0]
#     second_largest = -1
    
#     for i in arr:
#         if i > largest:
#             second_largest = largest 
#             largest = i
        
#     return second_largest

# # print(second_largest_element_practice(arr))


# def check_arr_sorted_practice(arr):
#     # Brute Approach
#     result = False
#     for i in range(len(arr) - 1):
#         if arr[i] < arr[i+1]:
#             result = True
#         else:
#             result = False
    
#     return result
    
# # print(check_arr_sorted_practice(arr))


# def remove_duplicates_practice(arr):
#     # Brute Approach
#     # arr = list(set(arr))
#     # return len(arr) - 1
    
#     # Optimal Approach
#     index = 0
#     for i in range(len(arr)):
#         if arr[i] != arr[index]:
#             arr[index + 1] = arr[i]
#             index += 1
        
#     return index + 1

# # print(remove_duplicates_practice(arr))




