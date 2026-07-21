class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
         total = 0
         end = 0
         for t in timeSeries:
            if t >= end:
                total += duration
            else:
                total += t + duration - end

            end = t + duration

         return total