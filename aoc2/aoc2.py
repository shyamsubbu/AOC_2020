from collections import Counter
import re
import unittest


class SolutionAoc2:

    def __init__(self, file):
        self.file = file

    def is_password_valid_aoc2_1(self):
        with open(self.file, 'r') as f:
            lines = f.readlines()
            no, v, s = 0, 0, set()
            for line in lines:
                no += 1
                p = re.compile(r'(\d+)-(\d+)\s(\S):\s([a-z]+)')
                m = p.search(line)
                sidx, eidx, char, ps = m.groups()
                c = Counter(ps)
                if char in c and c[char] in range(int(sidx), int(eidx) + 1):
                    v += 1
        return v

    def is_password_valid_aoc2_2(self):
        with open(self.file, 'r') as f:
            lines = f.readlines()
            no, v, s = 0, 0, set()
            for line in lines:
                no += 1
                p = re.compile(r'(\d+)-(\d+)\s(\S):\s([a-z]+)')
                m = p.search(line)
                sidx, eidx, char, ps = m.groups()
                c = Counter(ps)
                if char in ps and ((char in ps[int(sidx) - 1] and char not in ps[int(eidx) - 1]) or (char not in ps[int(sidx) - 1] and char in ps[int(eidx) - 1])):
                    v += 1
            return v


class TestSolutionAoc2(unittest.TestCase):

    def setUp(self):
        self.expectedaoc2_1 = 500
        self.expectedaoc2_2 = 313
        self.sln = SolutionAoc2('/Users/spudukko/AOC_2020/aoc2/efg.txt')

    def test_is_password_valid_aoc2_1(self):
        result = self.sln.is_password_valid_aoc2_1()
        self.assertEqual(result, self.expectedaoc2_1)

    def test_is_password_valid_aoc2_2(self):
        result = self.sln.is_password_valid_aoc2_2()
        self.assertEqual(result, self.expectedaoc2_2)

unittest.main(argv=[''], verbosity=2, exit=False)
