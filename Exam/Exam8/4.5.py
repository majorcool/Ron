# 4.5  Largest Perimeter Triangle
# Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of
# these lengths. If it is impossible to form any triangle of a non-zero area, return 0.
def largest_perimeter(nums: list) -> int:
    nums.sort(reverse=True)
    for a in range(0, len(nums)-2):
        if nums[a] - nums[a+1] < nums[a+2]:
            return nums[a] + nums[a+1] + nums[a+2]
    return 0


