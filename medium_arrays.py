arr = list(map(int, input("Enter array element: ").split())) or [2,6,5,11,8,11]

# Two Sum
# Brute Approach - looping through the array and checking for the summation to the target number
def twoSum(arr, target):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == target:
                return [i,j]
    
# print(twoSum(arr,14))

# Better Approach - Hashing method
def better_twoSum(arr,target):
    hash_map = {}
    
    for i in range(len(arr)):
        rest = target - arr[i]

        if rest in hash_map:
            return [hash_map[rest], i]
        
        hash_map[arr[i]] = i
        print(hash_map)
        
               
    return []

# print(better_twoSum(arr, 14))

# Optimal Approach - 2 pointer method
def optimal_twoSum(arr, target):
    left = 0
    right = len(arr)-1
    
    arr.sort()

    print(arr)
    while left < right:
        if arr[left] + arr[right] == target:
            return True
        elif (arr[left] + arr[right] ) < target:
            left += 1
        else:
            right -= 1
    return False

# print(optimal_twoSum(arr,11))

# Sort an Array of 0's, 1's and 2's
# Brute Approach - using any of the sorting algorithms
arr = [1,2,1,0,0,1,2,0,1]
low = 0
high = len(arr) - 1

def merge(arr, low, mid, high):
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
        arr[i] = temp[i-low]
    
def sort_arr(arr, low, high):
    # merge sort
    
    if low == high:
        return

    mid = (low + high) // 2
    sort_arr(arr, low, mid)
    sort_arr(arr, mid+1, high)
    merge(arr, low, mid, high)
    
    
    return arr


# print(sort_arr(arr, low, high))

# Better Approach - counting the 0's, 1's and 2's in the arr and store in place of the count0, count1, count2
arr = [1,2,1,0,0,1,2,0,1]
def better_sort_arr(arr):
    count0 = 0
    count1 = 0
    count2 = 0
    
    for i in arr:
        if i == 0:
            count0 += 1
        elif i == 1:
            count1 += 1
        else:
            count2 += 1
        
    for i in range(count0):
        arr[i] = 0
    
    for i in range(count1):
        arr[i+count0] = 1
    
    for i in range(count2):
        arr[i + count0 + count1] = 2

    return arr

# print(better_sort_arr(arr))

# Optimal Approach - using Dutch National Flag Algorithm
# Dutch National Flag Algorithm Rules:
# 1. range(0 - low - 1) - everything is 0 (sorted)
# 2. range(low, mid - 1) - everything is 1 (sorted)
# range(mid, high) - unsorted array
# 3. range(high + 1, len(arr) - 1) - everything is 2 (sorted)
arr = [1,2,1,0,0,1,2,0,1]
def optimal_sort_arr(arr):
    low = 0
    mid = 0
    high = len(arr) - 1
    
    for i in range(len(arr)):
        if arr[mid] == 0:
            arr[mid], arr[low] = arr[low], arr[mid]
            mid += 1
            low += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr

# print(optimal_sort_arr(arr))


# Majority Element in Array
# Brute Approach - iterating through the array and check the element count is greater than the lenght of array by 2
arr = [6,5,5]
def majority_element(arr):
    n = len(arr)
    for i in arr:
        count = 0
        for j in arr:
            if j == i:
                count += 1
            
        if count > n//2:
            return arr[i]
    
    return -1

print(majority_element)

# Better Approach - using Hash Map storing the arr element and number of times it present in the arr, 
#                   and again iterating through the map and seeing the element count > n//2 or can check the max, 
#                   maxelement variable with the value, element in the hashmap
def better_majority_element(arr):
    hash_map = {}
    
    for i in range(len(arr)):
        if arr[i] in hash_map:
            # print(arr[i])
            hash_map[arr[i]] += 1
        else:
            hash_map[arr[i]] = 1
    
    print(hash_map)
    max = 0
    maxelement = 0
    for element, value in hash_map.items():
        if value > max:
            max = value
            maxelement = element
            
    return maxelement
        
print(better_majority_element(arr))














