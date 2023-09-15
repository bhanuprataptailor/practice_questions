def quick_sort(A):
    i = 0
    j = 0
    pivot = len(A) - 1

    if len(A) <= 1:
        return A

    while j != pivot:
        if A[i] > A[pivot]:
            j += 1
        else:
            A[i], A[j] = A[j], A[i]
            i += 1
            j += 1

    A[pivot], A[i] = A[i], A[pivot]
    return quick_sort(A[:i]) + [A[i]] + quick_sort(A[i+1:])


print(quick_sort(A=[1, 4, 3, 2, 5, 6]))
