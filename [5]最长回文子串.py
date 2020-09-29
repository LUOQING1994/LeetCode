# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。 
# 
#  示例 1： 
# 
#  输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
#  
# 
#  示例 2： 
# 
#  输入: "cbbd"
# 输出: "bb"
#  
#  Related Topics 字符串 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        tmp_len = len(s)
        tmp_flag_arr = [[False for _ in range(tmp_len)] for _ in range(tmp_len)]
        if tmp_len <= 1:
            return s

        for i in range(0,tmp_len):
            for j in range(0, tmp_len):
                if i == j:
                    tmp_flag_arr[j][i] = True
        tmp_result = 1
        tmp_start = 0
        for i in range(1,tmp_len):
            for j in range(0, tmp_len - i):
                if s[j] == s[j + i]:
                    if i == 1:
                        tmp_flag_arr[j][j + i] = True
                        if tmp_result < i + 1:
                            tmp_result = i + 1
                            tmp_start = j
                    else:
                        if tmp_flag_arr[j + 1][j + i - 1]:
                            tmp_flag_arr[j][j + i] = True
                            if tmp_result < i + 1:
                                tmp_result = i + 1
                                tmp_start = j
        print(tmp_start , tmp_result)
        print(s[tmp_start : tmp_start + tmp_result])
        return s[tmp_start : tmp_start + tmp_result]

    def longestPalindrome1(self, s):
        tmp_len = len(s)
        if tmp_len <=1:
            return s

        dp = [[False for _ in range(0, tmp_len)]for _ in range(0, tmp_len)]
        for i in range(0, tmp_len):
            for j in range(0, tmp_len):
                if i == j:
                    dp[i][j] = True

        tmp_str_len = 0
        tmp_str_start = 0
        for i in range(1, tmp_len):
            for j in range(0, tmp_len - i):
                if s[j] == s[j + i]:
                    if i == 1:
                        dp[j][j+i] = True
                        if tmp_str_len < i + 1:
                            tmp_str_len = i + 1
                            tmp_str_start = j
                    else:
                        if dp[j + 1][j + i - 1]:
                            dp[j][j + i] = True
                            if tmp_str_len < i + 1:
                                tmp_str_len = i + 1
                                tmp_str_start = j
        print(s[tmp_str_start : tmp_str_start + tmp_str_len])
        return s[tmp_str_start : tmp_str_start + tmp_str_len]



# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    obj = Solution()
    str = "cbbd"
    obj.longestPalindrome1(str);