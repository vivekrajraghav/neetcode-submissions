class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        i=0
        j=n-1
        while j>i:
            if target>numbers[i]+numbers[j]:
                i+=1
            elif target<numbers[i]+numbers[j]:
                j-=1
            elif target==numbers[i]+numbers[j]:
                return [i+1,j+1]
        return
    