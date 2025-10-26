#Question 1716 (Leetcode): Calculate Money in Leetcode Bank - Solution 2 (Optimal)
class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        first_week = 28
        last_week = 28 + 7 * (weeks -1)
        res = weeks * (first_week + last_week) // 2 #use the gauss formula

        #Calculate the days remaining left. For example: 30 days: 4 weeks + 2 days left.
        #Those 2 days are from week 5, so that why mondays = weeks + 1
        monday = weeks + 1
        for i in range(n % 7):
            res += i + monday

        return res