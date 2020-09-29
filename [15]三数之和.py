# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复
# 的三元组。 
# 
#  注意：答案中不可以包含重复的三元组。 
# 
#  
# 
#  示例： 
# 
#  给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# 
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
#  
#  Related Topics 数组 双指针

'''
    解题思路：
            1，从小到大排序
            2，设置三个指针 i 、L 、R 其中：L = i + 1, R = len(nums) - 1
            3, 由于排序的原因 当nums[i]>0时 程序可直接跳出循环
            4，当nums[i] + nums[L] + nums[R] 大于0时 R向前移动 否则L向后移动 当等于0时 判断L后面 和 R前面的数是否相等 进而排除重复值
'''
# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 排序
        if nums =="" or len(nums) < 3:
            return []
        nums.sort()
        result = []
        for i in range(0, len(nums)):
            R = len(nums) - 1
            L = i + 1
            if nums[i] > 0:
                return result
            if i != 0 and nums[i] == nums[i-1]:
                continue
            while L < R:
                tmp_sum = nums[i] + nums[L] + nums[R]
                if tmp_sum == 0:
                    result.append([nums[i] , nums[L] , nums[R]])
                    while L < R and nums[L] == nums[L+1]:
                        L += 1
                    while L < R and nums[R] == nums[R-1]:
                        R -= 1
                    L += 1
                    R -= 1
                elif tmp_sum > 0:
                    R -= 1
                else:
                    L += 1
        return result
    def threeSum1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 排序
        if nums =="" or len(nums) < 3:
            return []
        nums.sort()
        result = []
        for i in range(0, len(nums)):
            last_index = len(nums) - 1
            j = i + 1
            while j < last_index:
                if nums[i] <= 0:
                    rmp_sum = nums[i] + nums[j] + nums[last_index]
                    if rmp_sum == 0:
                        if not result.__contains__([nums[i] , nums[j] , nums[last_index]]):
                            result.append([nums[i] , nums[j] , nums[last_index]])
                        j += 1
                    elif rmp_sum > 0:
                        last_index = last_index - 1
                    else:
                        j += 1
                else:
                    break
        return result
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    obj = Solution()
    print(obj.threeSum([-1, 0, 1, 2, -1, -4]))