# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。 
# 
#  示例 1: 
# 
#  输入: "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#  
# 
#  示例 2: 
# 
#  输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#  
# 
#  示例 3: 
# 
#  输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#  
#  Related Topics 哈希表 双指针 字符串 Sliding Window


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    # def lengthOfLongestSubstring(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     tmp_hash = {}
    #     result = 0
    #     for i in range(0,len(s)):
    #         if tmp_hash.get(s[i]) is not None:
    #             result = max(result, len(tmp_hash))
    #             if tmp_hash.get(s[i]) is not None:
    #                 tmp_hash.pop()
    #         else:
    #             tmp_hash[s[i]] = i
    #     result = max(result, len(tmp_hash))
    #     return result

    """
        思路：使用双指针模拟滑动窗口
        1，p_end表示子字符串的结束位置 该指针从左向右依次滑动
        2，截取p_start 和 p_end之间的字符串 查看s[p_end]字符是否在该字符串中
        3，在该字符串中 则改变p_start的位置指向重复元素 同时统计一下该字符串的长度max(result,p_end - p_start)不在 则重复第一步
        最后 取出最大长度即可
        注意：在改变p_start时 需要采用这样的方式：p_start = p_start + tmp_str.index(s[p_end]) + 1
    """
    def lengthOfLongestSubstring(self, s):
        len_str = len(s)
        # 使用双指针模拟滑动窗口
        p_start = 0
        p_end = 0
        result = 0
        if len_str <=1:    # 判断临界条件
            return len_str
        while p_end < len_str:
            tmp_str = s[p_start: p_end]
            if s[p_end] in tmp_str:
                result = max(result,p_end - p_start)
                p_start = p_start + tmp_str.index(s[p_end]) + 1
            p_end = p_end + 1
        return max(result, p_end - p_start)



if __name__ == '__main__':
    obj = Solution()
    print(obj.lengthOfLongestSubstring("abcabcbb"))
# leetcode submit region end(Prohibit modification and deletion)
