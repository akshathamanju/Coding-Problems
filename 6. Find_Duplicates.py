'''
sort the array and chech if ith element is equal to i-1th element

time: complexity: O(nlogn) -> sort 
spce complexity: O(1) -> in place sorting
find the duplicates in the array


'''
def find_duplicates1(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return nums[i]

print('Approach 1')        
arr = [1, 2, 3, 4, 5 , 6, 3]
print(find_duplicates1(arr))

'''

create a dictionary and add each elements to the dictionaty
time: complexity: O(n)
spce complexity: O(n) creating a dictionay will take n space
'''
 
def find_duplicates2(nums):
    my_dict = dict()
    for num in nums:
        if num in my_dict:
            return num
        my_dict[num] = 1
print('Approach 2')     
arr = [1, 2, 3, 4, 5 , 6, 3]
print(find_duplicates2(arr))


'''



'''
def find_duplicates3( nums):
        # find the intersection point of 2 runners
        slow = fast = nums[0]
     
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
            if slow == fast:
                break
                
        # find the entrace to the cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return fast
print('Approach 3')     
arr5 = [1, 2, 3, 4, 5 , 6, 3]

print(find_duplicates3(arr5))

nums5 = [1, 2, 3, 4, 5 , 6, 3]
print('printting array 5')
for i in range(len(nums5)):
    print(nums5[nums5[i]], i)


