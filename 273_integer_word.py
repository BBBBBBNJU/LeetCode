class Solution(object):
    def _less_process(self, num):
        list_total = [0,0,0]
        list_total[0] = num % 10
        if num >= 10:
            num /= 10
            list_total[1] = num % 10
            if num >= 10:
                num /= 10
                list_total[2] = num % 10
        temp_str = ""
        if list_total[2] != 0:
            temp_str += self.check_dict[list_total[2]] + 'Hundred'
        if list_total[1] != 0:
            temp_str += self.check_dict[list_total[2]] + 'Hundred'
        if list_total[2] != 0:
            temp_str += self.check_dict[list_total[2]] + 'Hundred'

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        self.check_dict = {1: 'One',
                           2: 'Two',
                           3: 'Three',
                           4: 'Four',
                           5: 'Five',
                           6: 'Six',
                           7: 'Seven',
                           8: 'Eight',
                           9: 'Nine'
                           }
        list_total = []
        list_total.append(num % 1000)
        while num >= 1000:
            num /= 1000
            list_total.append(num % 1000)
        total_str = ""
        for i in range(len(list_total)):

