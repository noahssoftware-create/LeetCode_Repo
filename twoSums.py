nums = [2,7,11,15]
target = 9
def twoSum(target, nums):
    hashmap = {}
    for i, num in enumerate(nums):
        answer = target - num
        if answer in hashmap:
            print(f"{num}, {answer}")
            print(f"Indices: [{hashmap[answer], i}]")
            return [hashmap[answer],i]
        else:
            hashmap[num] = i
twoSum(target,nums)