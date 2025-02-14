# 将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。 
# 
#  比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下： 
# 
#  L   C   I   R
# E T O E S I I G
# E   D   H   N
#  
# 
#  之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。 
# 
#  请你实现这个将字符串进行指定行数变换的函数： 
# 
#  string convert(string s, int numRows); 
# 
#  示例 1: 
# 
#  输入: s = "LEETCODEISHIRING", numRows = 3
# 输出: "LCIRETOESIIGEDHN"
#  
# 
#  示例 2: 
# 
#  输入: s = "LEETCODEISHIRING", numRows = 4
# 输出: "LDREOEIIECIHNTSG"
# 解释:
# 
# L     D     R
# E   O E   I I
# E C   I H   N
# T     S     G 
#  Related Topics 字符串


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # 边缘条件
        if numRows < 2: return s
        res = ["" for _ in range(0,numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1:
                flag = - flag
            i = i + flag
        return "".join(res)

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    str = "LEETCODEISHIRING"
    numRows = 3
    obj = Solution()
    print(obj.convert(str, 3))