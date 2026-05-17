arr = list(map(int, input("Enter array element: ").split())) or [100,102,100,101,101,4,3,2,3,2,1,1,1,2]

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

# print(majority_element)

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
    
    # print(hash_map)
    max = 0
    maxelement = 0
    for element, value in hash_map.items():
        if value > max:
            max = value
            maxelement = element
            
    return maxelement
        
# print(better_majority_element(arr))


# Optimal Approach - Moore's Voting Algorithm
def optimal_majority_element(arr):
    maj_element = arr[0]
    count = 0
    n = len(arr)
    
    for i in range(len(arr)):
        # print(count)
        if count == 0:
            count = 1
            maj_element = arr[i]
        elif arr[i] == maj_element:
            count += 1
        else:
            count -= 1
        
    return maj_element

# print(optimal_majority_element(arr))

# Maximum Subarray sum in an array
# Brute Approach
def max_subarray_sum(arr):
    max = 0
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            sum = 0
            for k in arr:
                sum += k
                if sum > max:
                    max = sum
    
    return max

# print(max_subarray_sum(arr))

# Better Approach
def better_max_subarray_sum(arr):
    
    max = arr[0]
    
    for i in range(len(arr)):
        sum =0
        for j in range(i,len(arr)):
            sum += arr[j]
           
            if sum > max:
               max = sum
        
    return max
            

# print(better_max_subarray_sum(arr))


# Optimal Approach - Kadane's Algorithm
def optimal_max_subarray_sum(arr):
    
    sum = 0
    max = arr[0]
    
    for i in range(len(arr)):
        sum += arr[i]
        
        if sum > max:
            max = sum
        
        if sum < 0:
            sum = 0
            
    return max

# print(optimal_max_subarray_sum(arr))


# Printing Subarray with max subarray sum
def print_subarray_max_sum(arr):
    sum = 0
    max = float('-inf')
    ansStart = -1
    ansEnd = -1
    
    for i in range(len(arr)):
        if sum == 0:
            start = i
            
        sum += arr[i]
        
        if sum < 0: 
            sum = 0
        
            
        if sum > max:
            max = sum
            ansStart = start
            ansEnd = i
        
            
    temp = []
    for i in range(ansStart,ansEnd+1):
        temp.append(arr[i])
    
    return temp

# print(print_subarray_max_sum(arr))

# Stock Buy and Sell
# Brute Approach
def buy_sell_stocks(arr):
    profit = 0
    for i in range(len(arr)):
        buy = arr[i]
        for j in range(i+1,len(arr)):
            sell = arr[j]
            
            if buy < sell and sell - buy > profit:
                profit = sell - buy
                print("buy:",buy,"sell:",sell,"profit:",profit, end="\n")
            # print("buy and sell:", sell-buy, "profit:",profit,end="\n\n")
    return profit

# print(buy_sell_stocks(arr))                

# Optimal Approach
def optimal_buy_sell_stocks(arr):
    profit = 0
    mini = arr[0]
    
    for i in range(1,len(arr)):
        cost = arr[i] - mini # sell - buy
        profit = max(profit, cost)
        mini = min(mini, arr[i])
                
    return profit

# print(optimal_buy_sell_stocks(arr))

# Rearrange array elements by sign - having same number of positive and negative elements in the array
# Brute Approach - my thinking
def rearrange_element_bysign(arr):
    positive = []
    negative = []
    for i in arr:
        if i >= 0:
            positive.append(i)
        else:
            negative.append(i)
        
    print(positive, negative)
    # pos = 0
    # neg = 0
    # for i in range(len(arr)):
    #     if i == 0 or i % 2 == 0:
    #         arr[i] = positive[pos]
    #         pos += 1
    #         print(arr[i])
    #     else:
    #         arr[i] = negative[neg]
    #         neg += 1
    
    for i in range(len(arr)//2):
        arr[2*i] = positive[i]
        arr[2*i+1] = negative[i]
    
    return arr

# print(rearrange_element_bysign(arr))
        
# Optimal Approach - taking new array and having 2 pointers (pos, neg), 
#                    the pointers point to the new array on the old and even index, 
#           the even index contains the positive element and odd index contains the negative element from the original array
def optimal_rearrange_element_bysign(arr):
    ans = [0] * len(arr)
    pos = 0
    neg = 1
    
    for i in range(len(arr)):
        if arr[i] < 0:
            ans[neg] = arr[i]
            neg += 2
        else:
            ans[pos] = arr[i]
            pos += 2
    
    return ans

# print(optimal_rearrange_element_bysign(arr))


# Rearrange array elements by sign - not having the same number of positive and negative elements in the array
def sec_variate_rearrange_element_bysign(arr):
    pos = []
    neg = []
    ans = [0] * len(arr)
    for i in arr:
        if i >= 0:
            pos.append(i)
        else:
            neg.append(i)
        
    if len(pos) > len(neg):
        for i in range(len(neg)):
            ans[2*i] = pos[i]
            ans[2*i+1] = neg[i]
        
        index = 2 * len(neg)
        for i in range(len(neg), len(pos)):
            ans[index] = pos[i]
            index += 1
    else:
        for i in range(len(pos)):
            ans[2*i] = pos[i]
            ans[2*i+1] = neg[i]
            
        index = 2 * len(pos)
        
        for i in range(len(pos), len(neg)):
            ans[index] = neg[i]
            index += 1
    
    return ans
        
# print(sec_variate_rearrange_element_bysign(arr))

# Next Permutation
# Optimal Approach - using the observation and algorithm
# Observations
# 1. Keeping the Longest Prefix match, finding the breaking point arr[i] > arr[i+1]
# 2. find the element greater than arr[i] and smaller elent which will be closer to the element
# [2 1 | 5 4 3 0 0] -> 1 is the arr[i] and the element should be greater than the 1 
#                       and smaller one so that it will be closest to 1 which is 3
# [2 3 | 5 4 1 0 0]
# 3. Try to place the rest in the sorted arrangement
# [2 3 | 5 4 1 0 0] -> sorting the rest of the array -> [2 3 0 0 1 4 5]
def next_permutation(arr):
    index = -1
    for i in range(len(arr)-2, -1, -1):
        if arr[i] < arr[i+1]:
            index = i
            break
        
        
    if index == -1:
        arr.reverse()
        return arr
        
    print("index:",index)
        
    for i in range(len(arr)-1, index, -1):
        if arr[i] > arr[index]:
            arr[i], arr[index] = arr[index], arr[i]
            break
    
        
    for i in range(index+1, len(arr)):
        for j in range(i+1, len(arr)):
            # print('i:', i, 'j:', j)
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
        
    return arr

# print(next_permutation(arr))

# Leader in an Array:
# Brute Approach - looping through the array and checking if the element is greater 
#                  than the elements right side of the element

def arr_leader(arr):
    leaders = []
    
    for i in range(len(arr)):
        count = True
        for j in range(i+1, len(arr)):
            
            if arr[i] < arr[j]:
                count = False
                break
            
        if count == True:
            leaders.append(arr[i])
        
    return leaders

# print(arr_leader(arr))

# Optimal Approach - iterating through the array and comparing the element with the 
#                    max of the elements in the right, and storing in the new array
# [10,22,12,3,0,6] - looping from the end and checking the element is greater than the max and 
#                    representing with max and appending into the elemnet
# [6,12,22] - reverse the arr -> [22,12,6]
def optimal_arr_leader(arr):
    ans = []
    maxi = float('-inf')
    for i in range(len(arr)-1, -1, -1):
        print(arr[i])
        if maxi < arr[i]:
            ans.append(arr[i])
            
        maxi = max(maxi,arr[i])
        print("maxi:",maxi)

    return ans

# print(optimal_arr_leader(arr))


# Longest Consecutive Sequence
# Brute Approach - [102,4,100,101,1,3,2,1,1] this arr having the subsequences [100,101,102], [1,2,3,4] 
#                  the longest among these sequence is [1,2,3,4], returns the length of the longest subsequence
def linear_search(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            return True
    
    return False

def longest_consecutive_sequence(arr):
    longest = 1
    for i in arr:
        x = i
        count = 1
        for j in arr:
            while linear_search(arr,x+1):
                x += 1
                count += 1
                
        longest = count 
        
    return longest

# print(longest_consecutive_sequence(arr))

# Better Approach - Sorting the array and looping through and checking if 
#                   the element is same as the lastsmaller and tracking the count
def better_longest_consecutive_sequence(arr):
    
    for i in range(len(arr)):
        for j in range(i):
            if arr[j] > arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
            
    print(arr)
    countCurr = 0
    lastSmaller = float('inf')
    longest = 1
    
    for i in range(len(arr)):
        if arr[i] - 1 == lastSmaller:
            countCurr += 1
            lastSmaller = arr[i]
            
        elif arr[i] != lastSmaller:
            lastSmaller = arr[i]
            countCurr = 1
        
        longest  = max(longest, countCurr)
    return longest

# print(better_longest_consecutive_sequence(arr))

# Optimal Approach
def optimal_longest_consecutive_sequence(arr):
    num_set = set(arr)
    longest = 0
    for num in num_set:
        if num - 1 not in num_set:
            count = 1
            while num + 1 in num_set:
                num += 1
                count += 1
            
            longest = max(longest, count)
        
    return longest

print(optimal_longest_consecutive_sequence(arr))


