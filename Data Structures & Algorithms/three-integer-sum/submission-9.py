class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort to make duplicate handling easier
        result = set()  # Use a set to avoid duplicate triplets
        
        def dfs(index, path, total):
            # Base Case: If we have selected 3 numbers
            if len(path) == 3:
                if total == 0:
                    result.add(tuple(path))  # Convert to tuple to store in set
                return

            # Explore further numbers
            for i in range(index, len(nums)):
                # Skip duplicates to avoid repeated triplets
                if i > index and nums[i] == nums[i - 1]:
                    continue
                
                dfs(i + 1, path + [nums[i]], total + nums[i])  # Recursive call

        dfs(0, [], 0)  # Start DFS from index 0 with an empty path and total sum 0
        return [list(triplet) for triplet in result]  # Convert set to list

        
        
            


        


       