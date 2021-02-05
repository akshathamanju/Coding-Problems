'''
Write a program that takes an array A and an index i rnto A, and rearranges the elements such
that all elements less than A[r] (the "pivot") appear first, followed by elements equal to the pivot,
followed by elements greater than the pivot

'''
def dutch_flag_partition(arr, pivot_index):

    pivot = arr[pivot_index]
    # First pass: group elernents smaller than pivot
    for i in range(len(arr)):
        # Look fot a smaller element,
        for j in range( i + 1, len(arr)):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                break
    # Second pass: group elernents larger than pivot.
    for i in reversed(range(len(arr))):
        # Look for a Targer element. Stop when we reach an efernent less than
        # pivot, since first pass has moved them to the start of A.

        for j in reversed(range(i)):
            if arr[j] > pivot:
                arr[i], arr[j] = arr[j], arr[i]
                break
            

arr = [0, 1, 2, 0, 2, 1, 1]
print(arr)
print(dutch_flag_partition(arr, 3))
print(arr)
print(dutch_flag_partition(arr, 2))
print(arr)
'''
time complexity: O(n*n) :because in the first pass when searching for each additional
element smaller than the pivot we start from the beginning, However, there is no reason to start
from so far back-we can begin from the last location we advanced to. (Similar comments hold for
the second pass.)
Space complexity: O(1)

To improve tirne complexity, we make a single pass and move all the elements less than the pivot
to the beginning. In the second pass we move the larger elements to the end. It is easy to perform
each pass in a single iteration, moving out-of-place elements as soon as they are discovered.

'''

def dutch_flag_partition( arr, pivot_index,):
    pivot = arr[pivot_index]
    #first pass: group elements smaller than pivot
    smaller = 0
    for i in range(len(arr)):
        if arr[i] < pivot :
            arr[i], arr[smaller] = arr[smaller], arr[i]
            smaller += 1
    #second pass: group elements larget than pivot
    larger = len(arr) - 1
    for i in reversed(range(len(arr))):
        if arr[i] > pivot:
            arr[i], arr[larger] = arr[larger], arr[i]
            larger -= 1
print('Approach 2')       
arr1 = [0, 1, 2, 0, 2, 1, 1]
print(arr1)
dutch_flag_partition(arr1, 3)
print(arr1)
arr1 = [0, 1, 2, 0, 2, 1, 1]
print(arr1)
dutch_flag_partition(arr, 2)
print(arr)
'''
The time complexity isO(n) and the space complexity is O(1)
The main difference is that
it performs classification into elements less than, equal to, and greater than the pivot in a single
pass. This reduces runtime, at the cost of a trickier implementation. We do this by maintaining four
subarrays: bottom (elements less than pivot), middle (elements equal to pivot), unclassified, ar.d top
(elements greater than pivot). Initially, all elements areinunclassified. We iterate through elements
inunclassified, andmove elements into one of bottom,mi.ddle, andtop groups according to the relative
order between the incoming unclassified element and the pivot.

'''



def dutch_flag_partition(arr, pivot_index):
    pivot = arr[pivot_index]
    # Keep the following invariants during partitioning:
# botton group: A[:sma]IerJ.
# niddle gtoup: lfsnal]er:equa7l.
# unc]assifi ed. group: A[equal: Targer] .
# top group: A[Targer: ] .
    smaller, equal, larger = 0, 0 , len(arr)
    # Keep iterating as -Iong as there is an unclassified elenent
    while equal < larger:
        # A[equa7] is the inconing unclassjfied element,
        if arr[equal] < pivot:
            arr[smaller], arr[equal] = arr[equal], arr[smaller]
            smaller, equal = smaller+1, equal+1
        elif arr[equal] == pivot:
            equal += 1
        else:# A[equal] > pivot.
            larger -= 1
            arr[equal], arr[larger] = arr[larger], arr[equal]

print('Approach 3')       
arr1 = [0, 1, 2, 0, 2, 1, 1]
print(arr1)
dutch_flag_partition(arr1, 3)
print(arr1)
arr1 = [0, 1, 2, 0, 2, 1, 1]
print(arr1)
print(dutch_flag_partition(arr, 2))
print(arr)
   
