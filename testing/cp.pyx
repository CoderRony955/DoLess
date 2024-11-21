def sum_numbers(list nums):
    cdef int i
    cdef int total = 0
    for i in nums:
        total += i
    return total


cpdef int fast_add(int a, int b):
    return a + b

cpdef int fast_sub(int a, int b):
    return a - b


