nums = [1,2,3,4,5,6,7,9]
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
        