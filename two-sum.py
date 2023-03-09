def twoSum(nums, target):
    for i in range(len(nums) - 1):
        result_list = []
        result_list.append(i)
        if target - nums[i] in nums[i+1:]:
            result_list.append(nums[i+1:].index(target-nums[i]) + i + 1)
            return result_list
nums = list(map(int,input().split()))
target = int(input())

print(twoSum(nums, target))