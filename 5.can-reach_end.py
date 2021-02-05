'''
Write a program which takes an array of n integers, where A[i] denotes the maximum you can
advance from index l, and retums whether it is possible to advance to the last index starting from
the beginning of the array.

'''

def can_reach_end(arr):
    furthest_reach_so_far, last_index = 0, len(arr) - 1

    i = 0
    while i <= furthest_reach_so_far and furthest_reach_so_far < last_index:
        furthest_reach_so_far = max(furthest_reach_so_far, arr[i] + i)
        #print((furthest_reach_so_far, arr[i] + i))
        i += 1
    return furthest_reach_so_far >= last_index

arr = [3,3,7,0,2,0,1]
print(can_reach_end(arr))

arr = [3,2,0,0,2,0,7]
print(can_reach_end(arr), arr)

arr1 = [2, 4, 1, 1, 0, 2, 3]
print(can_reach_end(arr1))

arr2 = [2,3,1,1,4]
print(can_reach_end(arr2))

'''
Time Complexity: O(n)
space complexity: O(1)

'''
