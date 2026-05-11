# Selection Sort - Sorting elements based on the minimum element in the array

arr = list(map(int, input("Enter array elements: ").split())) or [4,22,4,62,1,3,6,9]

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

# Quick Sort - Sorting Arrays using pivot
# Divide and Conquer Algorithm

def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high
    print("Pivot:",pivot)
    print("i:",i,"j:",j)
    
    while i < j:
        print(arr)
        # while i <= high and arr[i] <= pivot:
        #     i += 1
        
        # while j >= low and arr[j] > pivot:
        #     j -= 1
        
        while arr[i] <= pivot and i <= high - 1:
            i += 1
        
        while arr[j] > pivot and j >= low + 1:
            j -= 1
        
        print("i:",i,"j:", j,"\n")
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        
    arr[low], arr[j] = arr[j], arr[low]
    
    return j

def quick_sort(arr, low, high):
    if low < high:
        partition_index = partition(arr,low,high)
        print("Partition index:",partition_index)
        
        quick_sort(arr, low, partition_index - 1)
        quick_sort(arr, partition_index + 1, high)
    
    return arr
    
print(quick_sort(arr, low, high))































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

# def partition_practice(arr, low, high):
#     pivot = arr[low]
#     i = low
#     j = high
    
#     while i < j:
#         while i <= high and arr[i] <= pivot:
#             i += 1
        
#         while j >= low and arr[j] > pivot:
#             j -= 1
            
#         if i < j:
#             arr[i], arr[j] = arr[j], arr[i]
        
#     arr[low], arr[j] = arr[j], arr[low]
#     return j
        

# def quick_sort_practice(arr, low, high):
#     if low < high:
#         partition_index = partition_practice(arr, low, high)
#         quick_sort_practice(arr, low, partition_index-1)
#         quick_sort_practice(arr, partition_index + 1, high)
        
#         return arr

# print(quick_sort_practice(arr, low, high))