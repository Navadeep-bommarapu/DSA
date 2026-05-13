arr = list(map(int, input("Enter array elements: ").split())) or [1,2,5,4,3,6,7,9]

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
    

# print(second_largest_element(arr))

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

# print(better_second_largest_element(arr))

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

# Optimal Approach --> finding the first occurence of 0 and 
#                      assign the pointer to the index and loop from the i and when arr[i] != 0 
#                      then swap with j index and increment j
def optimal_move_zero_to_end(arr):                
    j = 0
    for index in range(len(arr)):
        if arr[index] == 0:
            j = index
            break
    
    print(arr)
    # while i < len(arr):
    #     if arr[i] != 0:
    #         arr[i], arr[j] = arr[j], arr[i]
    #         i += 1
    #         j += 1
    #     else:
    #         i += 1
    
    for i in range(j+1,len(arr)):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
            
        
    return arr

# print(optimal_move_zero_to_end(arr))

# Linear Search
# Brute Approach ---> looping through the array and finding the index of the num
def linear_search(arr,n):
    for i in arr:
        if i == n:
            return arr.index(i)
    
    return -1

# print(linear_search(arr, 4))

# Union of two Sorted Array
# Brute Approach - using the set to store every unique elements from both the arrays
# arr1 = [1,1,2,3,4,5], arr2 = [2,3,4,4,5] ---> union = [1,2,3,4,5]
# arr1 = [1,1,2,3,4,5]
# arr2 = [2,3,4,4,5,6]
def union_of_sorted_arrs(arr1, arr2):
    # temp = []
    # print(arr1, arr2)
    
    # for i in range(len(arr1)):
    #     if arr1[i] not in temp:
    #         temp.append(arr1[i])
        
    # for j in range(len(arr2)):
    #     if arr2[j] not in temp:
    #         temp.append(arr2[j])
    
    temp = set()
    for i in arr1:
        temp.add(i)
        
    for j in arr2:
        temp.add(j)
        
    union = list(temp)
        
    return union
            
# print(union_of_sorted_arrs(arr1, arr2))

# Optimal Approach - 
def optimal_union_of_sorted_arrs(arr1, arr2):
    temp = []
    
    i = 0
    j = 0
    while j < len(arr2) and i < len(arr1):
        if arr1[i] < arr2[j]:
            if arr1[i] not in temp:
                temp.append(arr1[i])
                
            i += 1
            
        else:
            if arr2[j] not in temp:
                temp.append(arr2[j])
                
            j += 1
            
    while i < len(arr1):
        if arr1[i] not in temp:
            temp.append(arr1[i])
        i += 1
    
    while j < len(arr2):
        if arr2[j] not in temp:
            temp.append(arr2[j])
        j += 1
                
    return temp
                
# print(optimal_union_of_sorted_arrs(arr1,arr2))

# Intersection of two sorted arrays
# Brute Approach - declaring the arr of size of 2nd arr and 
#                  keeping the value be of zeros and when the nested loop compares the element are equal 
#                  and check if the visited arr has 0 then add that to the temp arr
arr1 = [1,2,2,3,3,4,5,6,9]
arr2 = [2,3,3,5,6,6,7,8,9,9]
def intersection_sorted_arr(arr1, arr2):
    temp = []
    visited = [0] * len(arr2)
    
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j] and visited[j] == 0:
                temp.append(arr1[i])
                visited[j] = 1
                break
            if arr2[j] > arr1[i]:
                break
            
    return temp

# print(intersection_sorted_arr(arr1,arr2))

# Optimal Approach
def optimal_intersection_sorted_arr(arr1,arr2):
    i = 0
    j = 0
    temp = []
    
        
    while j < len(arr2) and i < len(arr1):
        if arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            temp.append(arr1[i])
            i += 1
            j += 1
        
    return temp

# print(optimal_intersection_sorted_arr(arr1, arr2))

# Fiirst Missing Positive
def firstMissingPositive(nums):
    # Brute Approach - Not working
    # maximum = max(nums)
    # for i in range(1, maximum + 1):
    #     if i in nums:
    #         return i
    
    # return maximum + 1
    
    # Optimal Approach
    s = set(nums)
    i = 1
    
    while True:
        if i not in s:
            return i
    
        i += 1
        

# print(firstMissingPositive([1,2,0]))

# Finding Duplicates - returning the index of the duplicates
# Brute Approach - two pointer and 
def findDuplicate(nums):
    # (Not Working)
    # j = 1
    # for i in nums:
    #     if i == nums[j]:
    #         return i
    #     j += 1 
    
# Optimal Approach - intializing set ds and looping the arr and seeing if the element is in the set or not, 
#                    if it is there then the duplicate is printed or else the element is added to the set
    s = set()
    
    for i in nums:
        if i in s:
            return i     
        s.add(i) 

# print(findDuplicate([1,3,2,4,2]))

# Finding the Missing Number - Finding the number missing in the arr
# Brute Approach - arr = [1,2,4,5] n = length of arr => 4, find the element missing in the arr within range 1, n
def finding_missing_number(arr, n):
            
    for i in range(1,n+1):
        if i not in arr:
            return i
    return -1

n = len(arr)
# print(finding_missing_number(arr,n))
    



































































































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




