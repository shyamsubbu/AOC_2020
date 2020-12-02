
  import unittest
  import math

  # This Solution assumes no duplicates and no negatives as per input data. If duplicates are involved, we can add hashing or have a counter with duplicate data
  # copy this and run this in a jupyter notebook 


  class SolutionAoc1:

      def __init__(self, file, sum):
          self.sum = sum
          self.nums = []
          with open(file, 'r') as f:
              q = f.read().split()
              self.nums = list(map(int, q))

      def find3sum(self):
          num = self.nums
          ans = []
          for idx in range(len(num) - 1):
              sum = self.sum - num[idx]
              b, c = self.find2sum(sum, num[idx + 1:])
              if b and c:
                  ans.extend([num[idx], b, c])
          return ans

      def find2sum(self, sum=0, num=[]):
          if not num:
              num = self.nums
          if not sum:
              sum = self.sum
          ans = (0, 0)
          for i in range(len(num)):
              if sum >= num[i]:
                  k = sum - num[i]
                  if k in num:
                      ans = [num[i], k]
                      return ans
          return ans


  class AocTestCase(unittest.TestCase):

      def setUp(self):
          self.aoc1 = SolutionAoc1(file='/Users/spudukko/abc.txt', sum=2020)
          self.expected2sum = [1191, 829]
          self.expected3sum = [945, 657, 418]

      def test_aoc1_2sum_positive_non_duplicates(self):
          result = self.aoc1.find2sum()
          self.assertListEqual(result, self.expected2sum)

      def test_aoc1_3sum_positive_non_duplicates(self):
          result = self.aoc1.find3sum()
          self.assertListEqual(result, self.expected3sum)

  unittest.main(argv=[''], verbosity=2, exit=False)
