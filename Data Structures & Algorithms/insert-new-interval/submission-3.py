class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Handle the case where the input list is empty
        if not intervals:
            return [newInterval]
        
        n = len(intervals)
        l, r = 0, n - 1
        
        # --- PHASE 1: BINARY SEARCH ---
        # Find the correct index 'l' to keep intervals sorted by their start times.
        # We compare the start of newInterval with the starts of existing intervals.
        while l <= r:
            mid = (l + r) // 2
            
            # If the new interval starts after the current midpoint interval...
            if newInterval[0] > intervals[mid][0]:
                l = mid + 1  # ...look in the right half
            else:
                r = mid - 1  # ...look in the left half
        
        # --- PHASE 2: INSERTION ---
        # Insert newInterval at index 'l'. This maintains the sorted order.
        # Note: This is an O(N) operation because Python shifts elements to the right.
        intervals.insert(l, newInterval)
        
        # --- PHASE 3: LINEAR MERGE ---
        # Now that we've inserted the interval, some might be overlapping.
        # We iterate through the sorted list once to combine them.
        res = []
        for interval in intervals:
            # If 'res' is empty, or if the current interval starts AFTER 
            # the last merged interval ends, there is NO overlap.
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                # There is an overlap (the current interval starts before the last one ends).
                # Merge them by extending the end time of the last interval in 'res'.
                # We use max() because the current interval might be swallowed by the previous one.
                res[-1][1] = max(res[-1][1], interval[1])
        
        return res


                





        