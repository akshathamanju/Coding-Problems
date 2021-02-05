'''
Write a program which takes as input a sorted array and updates it so that all duplicates have been
removed and the remaining elements have been shifted left to fill the emptied indices. Return the
number of valid elements. Many languages have library functions for performing this operationyou cannot use these functions.


Solution: Let A be the array and n its length. If we allow ourselves O(n) additional space, we can
solve the problem by iterating through A and recording values that have not appeared previously
into a hash table. (The hash table is used to determine if a value is new.) New values are also
written to a list. The list is then copied back into A.
Here is a brute-force algorithm that uses O(1) additional space-iterate through A, testing if A[l]
equals Ali + 7), and, if so, shift all elements at and after I + 2 to the left by one. lrVhen all entries are
equal,thenumberofshiftsis(n-l)+(n-2)+...+2+1.,i.e.,O(nz),wherezisthelengthofthe
arTay.
The intuition behind achieving a better time complexity is to reduce the amount of shifting.
Since the array is sorted, repeated elements must appear one-after-anothe1, so we do not need an
auxiliary data structure to check if an element has appeared already. We move just one element,
rather than an entire subarray, and ensure that we move it just once.
For the given example, (2,3,5,5,7,77,11,17,13), when processing the A[3], since we already
have a 5 (which we know by comparing Al3l with A[2]), we advance to A141. Since this is a new
value, we move it to the first vacant entry, namely A[3]. Now the array is <2,3,5,7,7,11.,1,'1,,11.,\3),
and the first vacant entry is A[ ]. We continue from A[5].
'''
def delete_duplicates_from_sorted_array(arr):
    if not arr:
        return 0
    write_index = 1
    for i in range(1, len(arr)):
        if arr[write_index - 1] != arr[i]:
            #print(arr[write_index])
            arr[write_index] = arr[i]
            #print(arr[write_index], arr[i])
            write_index += 1
    return write_index

list1 = [2,3,5,5,7,11,11,11,13]
print(delete_duplicates_from_sorted_array(list1))
#delete_duplicates_from_sorted_array(list1)
