import data
import lab5
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    #    Part 1 tests should be in data_tests.py.

    # Part 2
    #    Part 2 tests should be in data_tests.py.


    # Part 3
    def test_time_add1(self):
        variable1 = data.Time(7, 54, 23)
        variable2 = data.Time(3, 21, 54)
        result = lab5.time_add(variable1, variable2)
        expected = data.Time(11, 16, 17)
        self.assertEqual(result, expected)

    def test_time_add2(self):
        variable1 = data.Time(3, 21, 3)
        variable2 = data.Time(4, 9, 23)
        result = lab5.time_add(variable1, variable2)
        expected = data.Time(7, 30, 26)
        self.assertEqual(result, expected)



    # Part 4
    def test_is_descending1(self):
        test_list = [10, 4, 3, 5, 2, 1]
        result = lab5.is_descending(test_list)
        expected = False
        self.assertEqual(result, expected)

    def test_is_descending2(self):
        test_list = [10, 8, 6, 5, 2, 1]
        result = lab5.is_descending(test_list)
        expected = True
        self.assertEqual(result, expected)



    # Part 5
    def test_largest_between1(self):
        test_list = [3, 5, 100, 7, 8, 23, 34, 56, 3, 1, 2, 56, 7, 99, 80, 34]
        lowertest = 5
        uppertest = 15
        result = lab5.largest_between(test_list, lowertest, uppertest)
        expected = 13
        self.assertEqual(result, expected)

    def test_largest_between2(self):
        test_list = [3, 5, 100, 7, 8, 23, 34, 56, 3, 1, 2, 56, 7, 99, 80, 34]
        lowertest = 1
        uppertest = 9
        result = lab5.largest_between(test_list, lowertest, uppertest)
        expected = 2
        self.assertEqual(result, expected)


    # Part 6
    def test_furthest_from_origin1(self):
        test_list = [data.Point(3, 5), data.Point(0, 1), data.Point(13, 20), data.Point(9, 2), data.Point(4, 7)]
        result = lab5.furthest_from_origin(test_list)
        expected = 2
        self.assertEqual(result, expected)

    def test_furthest_from_origin2(self):
        test_list = [data.Point(6, 2), data.Point(2, 5), data.Point(5, 3), data.Point(9, 10), data.Point(2, 1)]
        result = lab5.furthest_from_origin(test_list)
        expected = 3
        self.assertEqual(result, expected)





if __name__ == '__main__':
    unittest.main()
