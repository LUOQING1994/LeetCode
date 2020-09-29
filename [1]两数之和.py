# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。 
# 
#  你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。 
# 
#  
# 
#  示例: 
# 
#  给定 nums = [2, 7, 11, 15], target = 9
# 
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
#  
#  Related Topics 数组 哈希表


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0,len(nums)):
            tmp_value = target - nums[i]
            for j in range(0,len(nums)):
                if (i != j) and (nums[j] == tmp_value):
                    return [i,j]
        return -1

    def twoSum1(self, nums, target):
         for i in range(0,len(nums)):
            tmp_index = target - nums[i]
            if tmp_index in nums:
                if not((nums.count(tmp_index) == 1) and (tmp_index == nums[i])):
                    return [i, nums.index(tmp_index, i+1)]
         return []
    def twoSum2(self, nums, target):
         for i in range(0,len(nums)):
            tmp_value = target - nums[i]
            tmp_nums = nums[:i]  # 截取数组时 去除了第i个数 避免出现同一个数使用两次的情况
            if tmp_value in tmp_nums:
                return [tmp_nums.index(tmp_value), i]
         return []
    def twoSum3(self, nums, target):
        nums_hash = {}
        for key,value in enumerate(nums,1):  # 构建哈希表
            nums_hash[value] = key
        for key,value in enumerate(nums, 1):
            if nums_hash.get(target - value) is not None and key != nums_hash.get(target - value):
                return [key -1 , nums_hash.get(target - value) - 1]
    def twoSum4(self, nums, target):
        nums_hash = {}
        for key, value in enumerate(nums):
            if nums_hash.get(target - value) is not None:
                return [nums_hash.get(target - value), key]
            nums_hash[value] = key
        return -1
if __name__ == '__main__':
    obj = Solution()
    print(obj.twoSum4([2,7,11,15], 16))
        
# leetcode submit region end(Prohibit modification and deletion)
