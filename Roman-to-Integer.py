class Solution(object):
    def romanToInt(self, s):
        numbers=[]
        roman = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        letters = list(s)
        for char in letters:
            numbers.append(roman[char])
        total = 0
        for i in range(len(numbers)-1):
            if numbers[i] < numbers[i + 1]:
               total -= numbers[i]
            else:
                total += numbers[i]
        total += numbers[-1] 
        return total
