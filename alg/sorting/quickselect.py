from alg.sorting import partition
import random

# Quickselect algorithm: find the kth largest element in an array in O(n) avg-time and O(1) space.

# A: array of integers
# l, r: the range of elements to consider [l, r], where l <= r
# k: specifies the kth largest element desired, where 1 <= k <= r + 1
def quickselect(A, l, r, k):
    # Approach: Randomly choose a pivot and partition elements around it (smaller
    # to left, larger to right).  If that's the kth lagest element, you're done.
    # Otherwise, recurse to find the kth largest on one of the two sides.  

    # In particuar, let p be the random element of A selected in qsel(A, l, r, k)
    # and i it's index (0-indexed) after partitioning. And let k' = r - k + 1, the 
    # would-be index of the kth largest elem. Then:
    # qsel(A, l, r, k) = p if i = k' 
    # qsel(A, l, r, k) = qsel(A, l, i-1, k - (r - i + 1)) if k' < i
    # qsel(A, l, r, k) = qsel(A, i+1, r, k) if k' > i 


    # partiton around a random element 
    rand_idx = random.randrange(l, r + 1)
    i = partition.partition(A, l, r, rand_idx)
    # print(f'l: {l}, r: {r}, k: {k}, i: {i}') 
    # print(f'A: {A}')

    # recursive cases
    if (i == r - k + 1):
        return A[i]
    elif(i < r - k + 1):
        return quickselect(A, i + 1, r, k)
    else:
        return quickselect(A, l, i - 1, k - (r - i + 1))

