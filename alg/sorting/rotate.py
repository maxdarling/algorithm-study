def rotate(A, k):
    """Rotate an array's elements to the left by a specified amount.

    Args: 
        A: array of integers.
        k: integer amount to rotate. can be negative. 

    Returns:
        A reference to A, the modified array.
    """

    # todo: describe algorithm / reasoning.

    # key points: 
    # - frame the problem as a graph. indices as nodes and swaps as directional
    # edges.
    # - the graph has cycles that depend on n and k.
    # - I think # cycles = min(k, n - k) 
    # - if k = 1 or n % k == 0, there will be a single cycle that covers all
    # nodes
    # - otherwise, there will be multiple cycles. 
    # - Alg: iterate indices in increasing order, fully traverse cycles as you
    # encounter them, and stop after n_cycles iterations.
    # - to prove why alg works, have to prove that the first n_cycles nodes are
    # all on different cycles.

    if (len(A) == 0 or k % len(A) == 0):
        return A

    # remove redundant rotations
    k = k % len(A)

    # rotate right by k <-> rotate left by n - k
    if (k < 0):
        k += len(A)

    # calc # of cycles. 
    # (slightly arcane perhaps, but you can see why on paper?)
    n_cycles = min(k, len(A) - k)
    if (len(A) % n_cycles != 0):
        n_cycles = 1

    for i in range(n_cycles):
        curr = i
        # traverse the cycle starting at i, once around
        while True:
            next_idx = curr - k
            if (next_idx < 0):
                # wrap
                next_idx += len(A)

            A[i], A[next_idx] = A[next_idx], A[i]
            curr = next_idx

            if (curr == i):
                break

    return A

