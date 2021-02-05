'''
Write a program which takes as input an array of digits encoding a nonnegative decimal integer
D and updates the array to represent the integer D + 1. For example, if the input is (7,2,9) then
you should update the array to (1,3,0). Your algorithm should work even if it is implemented in a
langua ge that has finite-precision arithmetic.

arr = [ 9, 9]  -> add one to last element
          +1
    if the sum not eqaul to 10 go for the next ele
    else add 0 to the arr[i]
    add +1 to arr[i-1]

    if arr[0] = 10, ie we need to add 2 digits to the array insted of adding it at the begging add 1 the beginning and 0 to the end


'''


def plus_one(arr):
    arr[-1] += 1
    for i in reversed(range(1,len(arr))):
        if arr[i] != 10:
            break
        arr[i] = 0
        arr[i - 1] += 1
        # There is a carry-out, so we need one more digit to store the resu-It
        # A slick way to do this is to append a 0 at the end of the array,
        # and update the fjrst entry to 1.
    
        if arr[0] == 10:
            arr[0] = 1
            arr.append(0)
    return arr


arr = [1, 9, 9]
print(plus_one(arr))
arr = [ 9, 9]
print(plus_one(arr))
arr = [1, 9, 9, 9]
print(plus_one(arr))


'''
Time Complexity: O(n) -> n is length of array

'''
