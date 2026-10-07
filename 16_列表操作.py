nums = [5,2, 6,4,9]

print(nums[1:3])
print(nums[:3])
print(nums[0:])
print(nums[-2:])

print(max(nums),min(nums),sum(nums),sum(nums)/len(nums))
nums.sort()
print(nums)
nums.reverse()
print(nums)
nums.sort(reverse=True)