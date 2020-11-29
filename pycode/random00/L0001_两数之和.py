from typing import List


#


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        other_dict = dict(zip(nums, range(len(nums))))
        for i, it in enumerate(nums):
            if target - it in nums:
                return [i, other_dict[target - it]]
        return []

if __name__ == '__main__':
    c = Solution()
    print(c.twoSum([2, 7, 10, 12], 9))
