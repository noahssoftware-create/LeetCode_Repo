nums = [1,2,3,1]
class Solution(object):
    results = False
    def containsDuplicates(nums):
            hashmap = {}
            for num in nums:
                if num in hashmap:
                    return True
                else:
                    hashmap[num] = num
    results = containsDuplicates(nums)
    print(f"It is {results} that theres a duplicate in this list!")
    containsDuplicates(nums)
        