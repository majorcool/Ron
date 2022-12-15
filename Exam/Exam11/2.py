# 2  Degree of an Array
# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of
# any one of its elements.
# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.
def find_shortest_subarray(nums: list[int]) -> int:
    idx = {}
    for i, n in enumerate(nums):
        if n in idx:
            idx[n] += [i]
        else:
            idx[n] = [i]
    degree = max([len(i) for i in idx.values()])
    return min([i[-1] - i[0] for i in idx.values() if len(i) == degree]) + 1


