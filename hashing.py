# Hashing
# Finding the occurence of a number in the list 
# arr = [1,2,1,3,2]
# 1 -> 2 times
# 2 -> 2 times
# 3 -> 1 time
# 4 -> 0 times

# Brute Force Approach
# arr = list(map(int, input("Enter list values: ").split()))
# number = list(map(int, input("Enter queries: ").split()))


def num_occurence(number, arr):
    count = 0
    for i in arr:
        if i == number:
            count += 1
    return count

# print(num_occurence(number=1, arr=[1,2,1,3,1,2]))

def hashing_number(number, arr):
    hash = {}
    
    for i in arr:
        if i in hash:
            hash[i] += 1
        else:
            hash[i] = 1
    
    for i in number:
        if i > max(arr):
            print(0)
        else:
            print(hash[i])
        
    
# hashing_number(number, arr)
# string = input("Enter the string: ")
# q = list(input("Enter queries: ").split())
# print(q)


# hashing_with_string(string, q)
def hashing_with_string(str, queries):
    hash = {}
    
    for i in str:
        hash[i] = hash.get(i,0) + 1
    
    for i in hash:
        print(f"{i} -> {hash[i]}")
    
    for query in queries:
        if hash.get(query):
            print(hash[query])
        else:
            print(0)
            
            
# hashing_with_string("string", "i")         

nums = [2,3,4]
target = 7

def twoSum(nums, target):
    hash_map = {}
    
    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in hash_map:
            return [hash_map[complement], i]
        
        hash_map[nums[i]] = i

# print(twoSum(nums, target))


# Finding the Highest and the Lowest frequency element in an array
arr = [10,5,10,15,10,5]

def highesh_lowest_frequency_elements(arr):
    hash_map = {}
    
    for i in arr:
        hash_map[i] = hash_map.get(i, 0) + 1
        
    highest = 0
    lowest = len(arr)
    print(hash_map.items())
    
    # for i in hash_map:
    #     print(f"{i} -> {hash_map[i]}")
    #     if hash_map[i] > highest:
    #         highest = i
    #     if hash_map[i] < lowest:
    #         lowest = i
            
    for element, count in hash_map.items():
        print(f'{element} -> {count}')
        if highest < count:
            highest = element
        if lowest > count:
            lowest = element
        
    return highest, lowest
    
        
# print(highesh_lowest_frequency_elements(arr))

# Contains Duplicates - check if the duplicates index distance <= k
# [1,0,1,1] --> {1: 0, 0: 1, 1: 2, 1: 3}
def containsNearbyDuplicate(nums, k):
    seen = {}
    
    for i in range(len(nums)):
        
        if nums[i] in seen and i - seen[nums[i]] <= k: # (0,2), (0,3), (2,3) duplicates at this index, 
#                                                      checking the index distance 
#                                                      2-0 <= 2 x 
#                                                      3-0 <= 2 x 
#                                                      3-2 <= k (correct)
            return True
        
        seen[nums[i]] = i
    return False

print(containsNearbyDuplicate([1,0,1,1],2))
