class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_list = {}
        most_freq_array = []
        for num in nums:
            if num in freq_list:
                freq_list[num] += 1
            else:
                freq_list[num] = 1
        bucket_list = []
        for _ in range(len(nums) + 1):
            bucket_list.append([])
        
        for freq in freq_list:
            bucket_list[freq_list[freq]].append(freq)
        
        for i in range(len(bucket_list) -1 , 0, -1):
            for num in bucket_list[i]:
                most_freq_array.append(num)
            if len(most_freq_array) == k:
                return most_freq_array



