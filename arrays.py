arr = list(map(int, input("Enter array elements: ").split())) or [1,2,2,2,3,3,5,7,8,8]

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
# Brute Approach
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
# Brute Approach
def remove_duplicates(arr):
    # i = -1
    # j = 0
    
    # while i < j:
    #     i += 1
    #     j += 1
    #     if j > len(arr)-1:
    #         return arr
    #     if arr[i] == arr[j]:
    #         arr.remove(arr[i])
    #         i -= 1
    
    
    unique_elements = []
    j = 0
    print(arr)
    for i in range(1,len(arr)):
        if j >= len(arr):
            return unique_elements
        print(arr[i])
        if arr[i] != arr[j]:
            if unique_elements.count(arr[i]) < 1:
                
                unique_elements.append(arr[i])
        
            
        j+=1
    return unique_elements

print(remove_duplicates(arr))







