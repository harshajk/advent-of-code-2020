import unittest
import itertools

def day1p1(filename):
    f = open(filename, "r")
    entries = [int(ent) for ent in set(f.read().split("\n"))]

    for ent in entries:
        reqrd = 2020 - ent
        if reqrd in entries:
            f.close()
            return reqrd * ent
    
    return -1

def day1p2(filename):
    f = open(filename, "r")
    entries = [int(ent) for ent in set(f.read().split("\n"))]

    permutations = itertools.permutations(entries,3)

    for a, b, c in permutations:
        if a + b + c == 2020:
            f.close()
            return a * b * c

    return -1

class TestDay1(unittest.TestCase):
    def test_day1p1_example(self):
        result = day1p1("input/day01test.txt")
        self.assertEqual(514579, result)

    def test_day1p1_actual(self):
        result = day1p1("input/day01.txt")
        self.assertEqual(864864, result)        

    def test_day1p2_actual(self):
        result = day1p2("input/day01.txt")
        self.assertEqual(281473080, result)        

if __name__ == '__main__':
    unittest.main()
