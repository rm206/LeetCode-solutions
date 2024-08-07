class Solution:
    def numberToWords(self, num: int) -> str:
        d = {
            -1: "",
            0: "Zero",
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety",
            100: "Hundred",
            1000: "Thousand",
            1000000: "Million",
            1000000000: "Billion",
        }

        def three_digit(num, div):
            nonlocal res

            if num//100 > 0:
                res.append(d[num//100])
                res.append("Hundred")
            num = num%100

            if num in d and num > 0:
                res.append(d[num])
            else:
                if num // 10 > 0:
                    res.append(d[(num//10) * 10])
                num = num % 10

                if num > 0:
                    res.append(d[num])
            
            res.append(d[div])
        
        def solver(num, div):
            if num < 1000:
                three_digit(num, -1)
                return 
            
            if num//div > 0:
                three_digit(num//div, div)
            solver(num%div, div//1000)
        
        if num == 0:
            return d[0]
        res = []
        solver(num, 1000000000)
        res = " ".join(res)
        res = res.strip()
        return res