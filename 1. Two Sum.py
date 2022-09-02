def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen={}
        for index,nos in enumerate(nums):
            if target-nos in seen:
                return seen[target-nos],index
            seen[nos]=index
        
        res=twoSum(nums,target)
        print(res)

nums=[2,7,11,15]
target=9