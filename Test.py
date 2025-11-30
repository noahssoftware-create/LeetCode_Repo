nums = [1,1,7,3,3]
target = 6

def twoSum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        answer = target - num
        if answer in hashmap:
            print(hashmap[answer], i)
            return hashmap[answer],i
        else:
            hashmap[num] = i

indexAnswer = twoSum(nums,target)
