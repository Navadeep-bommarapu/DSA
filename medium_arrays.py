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
low = 0
high = len(arr) - 1
arr = [1,2,1,0,0,1,2,0,1]

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
    
    if low >= high:
        return

    mid = (low + high) // 2
    sort_arr(arr, low, mid)
    sort_arr(arr, mid+1, high)
    merge(arr, low, mid, high)
    
    
    return arr


print(sort_arr(arr, low, high))