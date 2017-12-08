ass Solution(object):
    def _sub_isPoss(self, nums):
        if len(nums) < 3:
            return False
        min_num = nums[0]
        current_num = min_num
        all_freq = [0]
        freq_accum = [0]
        for eachone in nums:
            if eachone == current_num:
                all_freq[-1] += 1
                freq_accum[-1] += 1
            if eachone != current_num:
                current_num = eachone
                all_freq.append(1)
                freq_accum.append(freq_accum[-1])
                freq_accum[-1] += 1
        start_queue = [0] * all_freq[0]
        end_queue = []
        for i in range(len(all_freq)):
            if i == 0:
                if all_freq[i] > all_freq[i+1]:
                    k = all_freq[i] - all_freq[i+1]
                    end_queue += [i] * k
            elif i == len(all_freq)-1:
                if all_freq[i] > all_freq[i-1]:
                    k = all_freq[i] - all_freq[i-1]
                    start_queue += [i] * k
            else:
                if all_freq[i] > all_freq[i+1]:
                    k = all_freq[i] - all_freq[i+1]
                    end_queue += [i] * k
                if all_freq[i] > all_freq[i-1]:
                    k = all_freq[i] - all_freq[i-1]
                    start_queue += [i] * k
        end_queue += [len(all_freq) - 1] * all_freq[-1]    
        
        while(len(start_queue)!=0 and len(end_queue)!=0):
            temp_start = start_queue.pop(0)
            temp_end = end_queue.pop(0)
            if temp_end - temp_start < 2:
                return False
        return True
    
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sub_seq = [0]
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] > 1:
                sub_seq.append(i+1)
        sub_seq.append(len(nums))
        for i in range(len(sub_seq)-1):
            if not self._sub_isPoss(nums[sub_seq[i]:sub_seq[i+1]]) :
                return False
        return True
                
