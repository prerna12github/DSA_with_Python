class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        count1 = 0
        cand1 = 0
        count2 = 0
        cand2 = 0
        result = []
        f1 = 0
        f2 = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == cand1:
                count1 =count1+1
            elif nums[i] == cand2:
                count2 = count2+1    
            elif count1 == 0:
                cand1 = nums[i]
                count1 = 1
            elif count2  == 0:
                cand2 = nums[i]
                count2 = 1
            else:
                count1 = count1-1
                count2 = count2-1          

        for num in nums:
            if num == cand1:
                f1 = f1+1
            elif num == cand2:
                f2 = f2+1
        if f1 > n//3:
            result.append(cand1)
        if f2 > n//3:
            result.append(cand2)
        return result                

        