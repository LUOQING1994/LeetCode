# 给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。 
# 
#  请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。 
# 
#  你可以假设 nums1 和 nums2 不会同时为空。 
# 
#  
# 
#  示例 1: 
# 
#  nums1 = [1, 3]
# nums2 = [2]
# 
# 则中位数是 2.0
#  
# 
#  示例 2: 
# 
#  nums1 = [1, 2]
# nums2 = [3, 4]
# 
# 则中位数是 (2 + 3)/2 = 2.5
#  
#  Related Topics 数组 二分查找 分治算法


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findMedianSortedArrays1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = []
        nums1_len = len(nums1)
        nums2_len = len(nums2)
        while nums1_len !=0 and nums2_len != 0:
            if nums1[nums1_len - 1] > nums2[nums2_len - 1]:
                nums1_len = nums1_len - 1
                nums3.append(nums1[nums1_len])
                nums1.pop(nums1_len)
            else:
                nums2_len = nums2_len - 1
                nums3.append(nums2[nums2_len])
                nums2.pop(nums2_len)
        if nums1_len == 0 and nums2_len != 0:
            nums2.reverse()
            nums3 = nums3 + nums2
        elif nums1_len != 0 and nums2_len == 0:
            nums1.reverse()
            nums3 = nums3 + nums1
        if len(nums3) % 2 == 0:
            tmp_result = (nums3[len(nums3) // 2] + nums3[len(nums3) // 2 - 1]) / 2
        else:
            tmp_result = nums3[len(nums3) // 2]
        print(tmp_result)
        return tmp_result
    def findMedianSortedArrays2(self, nums1, nums2):
        len_A = len(nums1)
        len_B = len(nums2)
        mid = (len_A + len_B) // 2
        tmp_a = 0
        tmp_b = 0
        while mid > 0:
            if (tmp_a <= len_A - 1) and (nums1[tmp_a] < nums2[tmp_b]):
                tmp_a = tmp_a + 1
            elif (tmp_b <= len_B - 1) and (nums1[tmp_a] >= nums2[tmp_b]):
                tmp_b = tmp_b + 1
            mid = mid - 1
        if tmp_a == len_A:
            tmp_a = tmp_a - 1
        if tmp_b == len_B:
            tmp_b = tmp_b - 1
        if (len_A + len_B) % 2 == 0:
           mid = (nums1[tmp_a] + nums2[tmp_b]) / 2
        else:
            mid = min(nums1[tmp_a], nums2[tmp_b])
        print(mid)
        return mid

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        numsum = nums1 + nums2  # 将2个序列拼接
        numsum.sort()  # 排序
        if len(numsum) % 2 == 0:
            themidnum = float(numsum[len(numsum) // 2 - 1] + numsum[len(numsum) // 2]) / 2
        else:
            themidnum = float(numsum[len(numsum) // 2])
        return themidnum
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    obj = Solution()
    nums1 = [1 , 2]
    nums2 = [3 , 4]
    obj.findMedianSortedArrays1(nums1, nums2)