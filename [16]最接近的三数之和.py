# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和
# 。假定每组输入只存在唯一答案。
#
#
#
#  示例：
#
#  输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
#
#
#
#
#  提示：
#
#
#  3 <= nums.length <= 10^3
#  -10^3 <= nums[i] <= 10^3
#  -10^4 <= target <= 10^4
#
#  Related Topics 数组 双指针

"""
    解题思路：
        1，本题承接三个数和为0的算法题 先进行排序 然后设置三个指针 i 、L = i + 1、R = len(nums) - 1
        2, 当nums[i] == nums[i-1] (i !=0) 时，可跳过该次循环 因为重复值不需要再次执行
        3， 计算nums[i]、nums[L]、nums[R]与target的差值tmp_result 当tmp_result大于0时 R向前移 寻找可能存在的最小差值
            否则 L向后移 寻找可能存在的最小差值
        4， 比对可能的最小差值 记录全局最小值 输出
"""
# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        min_value = 999999
        for i in range(0, len(nums)):
            L = i + 1
            R = len(nums) - 1
            if i != 0 and nums[i] == nums[i -1]:
                continue
            while L < R:
                tmp_result = nums[i] + nums[L] + nums[R] - target
                if tmp_result > 0 :
                    R -= 1
                else:
                    L += 1
                if abs(min_value) > abs(tmp_result):
                    min_value = tmp_result

        return min_value + target
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    obj = Solution()
    print(obj.threeSumClosest([1,1,-1,-1,3], -1))