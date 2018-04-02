class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        result = 1
        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return 1
        for i in range(1, length):
            if nums[i] == nums[i - 1]:
                continue
            else:
                nums[result] = nums[i]
                result += 1
        return result


'''
#my code:
上面这种方法是不能处理像[1,1,2,3,1]这种的，只有当序列是递增的时候才成功
i = 1

    while i < len(nums):
        flag = False
        j = 0
        while j < i:
            if nums[j] == nums[i]:
                flag = True
                nums.pop(i)
                break
            j += 1
        if not flag:
            i += 1
    return len(nums)
'''


