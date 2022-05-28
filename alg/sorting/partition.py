def partition(A: list[int], left: int, right: int, pivot_idx: int) -> int:
    """Split an array on a given range into two groups relative to a
    pivot element. Elements smaller than the pivot end up on the 
    left, and those greater than or equal end up on the right. 

    Args:
        A: array of integers.
        left: beginning of the range to operate on. inclusive, e.g.
        [left,right].
        r: end of range to operate on. inclusive, e.g. [left,right].
        pivot_idx: index of the element around which to partition A. 

    Returns:
        The new index of the pivot element after partitioning.
    """
    # -- the "Lomuto" partition scheme -- 
    pivotVal = A[pivot_idx]
    A[pivot_idx], A[right] = A[right], A[pivot_idx] # temporarily shove pivot to end
    first_greater_idx = left

    # invariant: before any iteration i, the smaller elems are in
    # [left:first_greater_idx] and greater or equal elems are in
    # [first_greater_idx:i]. 
    for i in range(left, right):
       if (A[i] < pivotVal):
           A[i], A[first_greater_idx] = A[first_greater_idx], A[i]
           first_greater_idx += 1


    # swap pivot back into its correct place
    A[right], A[first_greater_idx] = A[first_greater_idx], A[right]
    return first_greater_idx

