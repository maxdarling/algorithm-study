from alg.sorting.quickselect import quickselect
import math

# [in progress]: currently works only under assumption of no duplicate
# elements
def wigglesort(A):
    if (len(A) <= 1): 
        return A

    quickselect(A, 0, len(A) - 1, len(A) // 2 + 1)
    print(f'partiitoned A: {A}')

    # interleave small and large elements according to: 
    # index-mapping:
    # if i < ceil(n/2) -> i = 2*i
    # if i >= ceil(n/2) -> i = 2 * (n - 1 - i) + 1 = 2*n - 2*i - 1

    # we can only run this once and hope its a full chain
    curr = 1
    start = 1
    while (True): 
        # 0->0 is implicit. 
        # Then, we swap 1 to 2. To ends up at 1. 
        # Then we swap the elem that was at 2, now at 1, to 4.
        # Then we swap the elem that was at 4, now at 1, to 5.
        # And so on. 1 is our temp swapping slot, and we'll stop
        # once the elem in idx 1 is meant to be there.
        new_idx = 2 * curr 
        if (curr >= math.ceil(len(A) / 2)):
            new_idx = 2 * (len(A) - 1 - curr) + 1

        print(f'curr: {curr}, new_idx: {new_idx}')
        A[start], A[new_idx] = A[new_idx], A[start]
        curr = new_idx
        if (curr == 1):
            break

    return A



a = [5, 6, 0, 3, 1, 2, 4]
print(f'result: {wigglesort(a)}')
b = [1,5,1,1,6,4]
print(f'result: {wigglesort(b)}')

# below are wrong due to duplicates. 

# outputs 1,2,2. 1, the last 2, then the first 2.
# the first 2 is classified as a L elem and the 2nd 2 an R.
# so it sees nothing wrong with L, R, L. 
# However, with an L/R scheme, no one number can be both L and R 
# or else this can happen
d = [1,2,2]
print(f'result: {wigglesort(d)}')

# this is impossible to solve with my alg. 
# if I adhered to above rule that no num can be both L/R, then
# we have 2 Ls and 4 Rs. But then that's impossible to arrange those
# in an alternating fashion. 
# in general, the possibility of duplicates leads to no guarantee
# that there's an equal # of Ls and Rs, so an alternating L/R
# scheme can't work.
e = [1,1,2,2,3,3]
print(f'result: {wigglesort(e)}')
