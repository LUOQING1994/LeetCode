# 编写一个函数来查找字符串数组中的最长公共前缀。 
# 
#  如果不存在公共前缀，返回空字符串 ""。 
# 
#  示例 1: 
# 
#  输入: ["flower","flow","flight"]
# 输出: "fl"
#  
# 
#  示例 2: 
# 
#  输入: ["flower","flow","flight"]
# 输出: ""
# 解释: 输入不存在公共前缀。
#  
# 
#  说明: 
# 
#  所有输入只包含小写字母 a-z 。 
#  Related Topics 字符串
'''
    解题思路：最长前缀串 必须从第一个字符开始 所以我们只需要遍历数组中其中一个字符即可
                1，统计相等的子前缀串的个数 等于字符数组长度即可继续遍历
                2，小于字符数组长度 则停止遍历
'''

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    # 查找最长公共字符串
    def longestCommonPrefix1(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) <= 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        tmp = strs[0]
        i , j = 1, 0
        max_str = ""
        while i <= len(tmp) and i != j:
            tmp_str = tmp[j : i]
            tmp_sum = 0
            for item in strs:
                if len(item.split(tmp_str)) >= 2:
                    tmp_sum += 1
            if tmp_sum != len(strs):
                j = i + 1
                i += 1
            else:
                max_str = tmp_str
                i += 1
        return max_str

    def longestCommonPrefix(self, strs):
        if len(strs) <= 0:
            return ""
        tmp = strs[0]
        i = 1
        max_str = ""
        while i <= len(tmp):
            tmp_str = tmp[0: i]
            tmp_sum = 0
            for item in strs:
                if item[0: i] == tmp_str:
                    tmp_sum += 1
            if tmp_sum == len(strs):
                max_str = tmp_str
                i += 1
            elif tmp_sum != len(strs):
                return tmp_str[0:-1]

        return max_str
    def longestCommonPrefix2(self, strs):
         res = ""
         for item in zip(*strs):
             tmp_set = set(item)
             if len(tmp_set) == 1:
                 res += item[0]
             else:
                 break
         return  res
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    obj = Solution()
    print(obj.longestCommonPrefix2(["flower","flowss"]))