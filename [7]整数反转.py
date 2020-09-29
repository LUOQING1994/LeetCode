# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。 
# 
#  示例 1: 
# 
#  输入: 123
# 输出: 321
#  
# 
#  示例 2: 
# 
#  输入: -123
# 输出: -321
#  
# 
#  示例 3: 
# 
#  输入: 120
# 输出: 21
#  
# 
#  注意: 
# 
#  假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231, 231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。 
#  Related Topics 数学


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # python 数组翻转   a = [1,2,3,4]  a.reverse() 或者 b = a[::-1]
        tmp_str = str(x)
        tmp_len = len(tmp_str)
        if tmp_len == 0:
            return 0
        result_array = ["" for _ in tmp_str]
        start_index, end_index = 0, tmp_len - 1
        if tmp_str[0] == "-":
            result_array[0] = "-"
            start_index = 1
        while start_index <= end_index:
            result_array[start_index] = tmp_str[end_index]
            result_array[end_index] = tmp_str[start_index]
            start_index += 1
            end_index -= 1
        tmp_result = int("".join(result_array))
        if (tmp_result >= -2 ** 31) and (tmp_result <= 2 ** 31):
            return tmp_result
        else:
            return 0
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    obj = Solution()
    print(obj.reverse(-123))