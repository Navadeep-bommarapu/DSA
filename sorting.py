# Selection Sort - Sorting elements based on the minimum element in the array

arr = list(map(int, input("Enter array elements: ").split())) or [0,1,2,3,4,24]

# Selection Sort - initializing the first element in the array and comparing to the other elements 
#                   and swapping with the minimum element in the array

def selection_sort(arr):
    print(arr)
    for i in range(len(arr)-1): # Ascending Order
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
                
        arr[i], arr[min] = arr[min], arr[i]
        
    # for i in range(len(arr)): # Descending Order
    #     min = i
    #     for j in range(i+1,len(arr)):
    #         if arr[j] > arr[min]:
    #             min = j
            
    #     arr[i], arr[min] = arr[min], arr[i]
    
    return arr

# print(selection_sort(arr))

# Bubble Sort - Pushs the maximum at the end of the array by adjacent swapping

def bubble_sort(arr):
    for i in range(len(arr)): # Ascending Order
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                
    # for i in range(len(arr)): # Descending Order
    #     for j in range(len(arr)-i-1):
    #         if arr[j] < arr[j+1]:
    #             temp = arr[j]
    #             arr[j] = arr[j+1]
    #             arr[j+1] = temp
                
    return arr

# print(bubble_sort(arr))


# Recursive Bubble Sort

# n = len(arr)

def recursive_bubble_sort(arr, n):
    
    if n == 1:
        return
    
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
        
        
    recursive_bubble_sort(arr, n-1)
    return arr
    
# print(recursive_bubble_sort(arr, n))


# Insertion Sort - Takes the element in the array and place it in the correct order
            
def insertion_sort(arr):
    for i in range(len(arr)):
        
        # My Brute force approach - didnt work
        
        # for j in range(i, -1, -1):
        #     if arr[j] < arr[j-1]:
        #         temp = arr[j]
        #         arr[j] = arr[j+1]
        #         arr[j+1] = temp
        
        j = i 
        while j > 0 and arr[j-1] > arr[j]:
            temp = arr[j-1]
            arr[j-1] = arr[j]
            arr[j] = temp
            j -= 1
            
    
    return arr

# print(insertion_sort(arr))

# Recursive Insertion Sort

# n = len(arr) 
# i = 0

def recursive_insertion_sort(arr, n, i):
    if i == n:
        return
    
    for index in range(i):
        if arr[index] > arr[i]:
            arr[index], arr[i] = arr[i], arr[index]
    
    recursive_insertion_sort(arr, n, i+1)
    return arr

# print(recursive_insertion_sort(arr, n, i))


# Merge Sort - Divide and Merge Technique
low = 0
high = len(arr) - 1

def merge(arr, low, mid,  high):
    temp = []
    
    left = low
    right = mid + 1
    
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
        
    while left <= mid:
        temp.append(arr[left])
        left += 1
    
    while right <= high:
        temp.append(arr[right])
        right += 1
    
    for i in range(low, high+1):
        arr[i] = temp[i - low]
        

def merge_sort(arr, low, high):
    if low >= high:
        return
    
    mid = (low + high) // 2
    
    merge_sort(arr, low, mid)
    merge_sort(arr, mid+1, high)
    merge(arr, low, mid, high)
    
    return arr

# print(arr)
# print(merge_sort(arr, low, high))

# Quick Sort
# def quick_sort(arr):
    
    
    
    
    
#     return arr

# print(quick_sort(arr))





# Finding the missing number from the length of nums
# [0, 2, 1, 3, 4] ouput: 5 is missing from the array range [0, 5]
def missingNumber(nums):
    
    # Brute Force
    # for i in range(len(nums)):
    #     for j in range(i):
    #         if nums[j] > nums[i]:
    #             temp = nums[i]
    #             nums[i] = nums[j]
    #             nums[j] = temp
                
    # print(nums)

    # for i in range(len(nums)):
    #     n = len(nums)
    #     if (i not in nums):
    #         return i
    #     elif (n not in nums):
    #         return n
    #     else:
    #         continue
        
    # Basic Math
    # Total summation of the expected array of range [0,n] would be n * (n+1) // 2
    # The array with the missing number will have the lesser value
    # By subtracting the expected sum and actual sum we get the answer
    
    n = len(nums)
    expected = n * (n+1) // 2
    return expected - sum(nums)
        
print(missingNumber(arr))









# def selection_sort_practice(arr):
#     for i in range(len(arr)-1):
#         min = i
#         for j in range(i+1,len(arr)):
#             if arr[min] > arr[j]:
#                 min = j
            
#         arr[i], arr[min] = arr[min], arr[i]
            
#     return arr

# # print(selection_sort_practice(arr))


# def bubble_sort_practice(arr):
#     for i in range(len(arr)):
        
#         j = i
#         while j > 0 and arr[j] < arr[j-1]:
#             # arr[j-1], arr[j] = arr[j-1], arr[j]
#             temp = arr[j-1]
#             arr[j-1] = arr[j]
#             arr[j] = temp
#             j -= 1
        
#     return arr

# # print(bubble_sort_practice(arr))

# def insertion_sort_practice(arr):
#     for i in range(len(arr)):
#         for j in range(i):
#             if arr[i] < arr[j]:
#                 temp = arr[i]
#                 arr[i] = arr[j]
#                 arr[j] = temp
                
#     return arr

# # print(insertion_sort_practice(arr))


# low = 0
# high = len(arr) - 1

# def merge_practice(arr, low, mid, high):
#     temp = []
    
#     left = low
#     right = mid + 1
    
#     while left <= mid and right <= high:
#         if arr[left] < arr[right]:
#             temp.append(arr[left])
#             left += 1
#         else:
#             temp.append(arr[right])
#             right += 1
    
#     while left <= mid:
#         temp.append(arr[left])
#         left += 1
        
#     while right <= high:
#         temp.append(arr[right])
#         right += 1
        
#     for i in range(low, high+1):
#         arr[i] = temp[i-low]
        

# def merge_sort_practice(arr, low, high):
#     if low >= high:
#         return
    
#     mid = (low + high) // 2
    
#     merge_sort_practice(arr, low, mid)
#     merge_sort_practice(arr, mid+1, high)
#     merge_practice(arr, low, mid, high)
    
#     return arr


# print(merge_sort_practice(arr,low,high))
