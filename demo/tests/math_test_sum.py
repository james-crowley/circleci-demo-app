import pytest
import time

class TestMathSum:
    # Math Operations for Testing Spliting
    @staticmethod
    def sum(a, b):
        return a + b

    # Sum Function Testing
    def test_sum_1_and_1(self):
        """Sum of 1 and 1"""
        output = self.sum(1, 1)
        assert output == 2

    def test_sum_neg_1_and_1(self):
        """Sum of -1 and 1"""
        output = self.sum(-1, 1)
        assert output == 0

    def test_sum_0_and_0(self):
        """Sum of 0 and 0"""
        output = self.sum(0, 0)
        assert output == 0

    def test_sum_neg_1_and_neg_1(self):
        """Sum of -1 and -1"""
        output = self.sum(-1, -1)
        assert output == -2

    def test_sum_1000000000_and_1(self):
        """Sum of 1000000000 and 1"""
        output = self.sum(1000000000, 1)
        assert output == 1000000001

    def test_sum_1000000000_and_1000000000(self):
        """Sum of 1000000000 and 1000000000"""
        output = self.sum(1000000000, 1000000000)
        time.sleep(120)
        assert output == 2000000000

    def test_sum_1000000000_and_neg_1000000000(self):
        """Sum of 1000000000 and -1000000000"""
        output = self.sum(1000000000, -1000000000)
        time.sleep(60)
        assert output == 0