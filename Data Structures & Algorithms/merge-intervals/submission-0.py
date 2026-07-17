class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def get_first(interval):
            return interval[0]
            
        sorted_intervals = sorted(intervals, key = get_first)
        new_sorted = []
        
        for i,arr in enumerate(sorted_intervals):
            if i > 0 and arr[0] <= new_sorted[-1][1]:
                new_sorted[-1][1] = max(arr[1], new_sorted[-1][1])
            else:
                new_sorted.append(arr)
        return new_sorted