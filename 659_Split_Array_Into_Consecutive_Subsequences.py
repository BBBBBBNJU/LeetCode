class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        min_num = nums[0]
        current_num = min_num
        all_freq = [0]
        for eachone in nums:
            if eachone == current_num:
                all_freq[-1] += 1
            if eachone != current_num:
                current_num = eachone
                all_freq.append(1)
        start_queue = [0] * all_freq[0]
        end_queue = []
        for i in range(len(all_freq)):
            if i == 0:
                if all_freq[i] > all_freq[i + 1]:
                    k = all_freq[i] - all_freq[i + 1]
                    end_queue += [i] * k
            elif i == len(all_freq) - 1:
                if all_freq[i] > all_freq[i - 1]:
                    k = all_freq[i] - all_freq[i - 1]
                    start_queue += [i] * k
            else:
                if all_freq[i] > all_freq[i + 1]:
                    k = all_freq[i] - all_freq[i + 1]
                    end_queue += [i] * k
                if all_freq[i] > all_freq[i - 1]:
                    k = all_freq[i] - all_freq[i - 1]
                    start_queue += [i] * k
        end_queue += [len(nums) - 1] * all_freq[-1]
        print (start_queue)
        print(end_queue)
        while (len(start_queue) != 0 and len(end_queue) != 0):
            temp_start = start_queue.pop(0)
            temp_end = end_queue.pop(0)
            if temp_end - temp_start < 2:
                return False
        if (len(start_queue) != 0 or len(end_queue) != 0):
            return False
        return True

solu = Solution()
a = [1, 2, 3, 4, 4,5]
winner = solu.isPossible(a)
print(winner)
