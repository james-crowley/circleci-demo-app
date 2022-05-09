import pytest
import time

class TestMathSub:
    # Math Operations for Testing Spliting
    @staticmethod
    def sum(a, b):
        return a + b

    # Sub Function Testing
    def test_sub_1_and_1(self):
        """Sub of 1 and 1"""
        output = self.sub(1, 1)
        assert output == 0

    def test_sub_neg_1_and_1(self):
        """Sub of -1 and 1"""
        output = self.sub(-1, 1)
        assert output == -2

    def test_sub_0_and_0(self):
        """Sub of 0 and 0"""
        output = self.sub(0, 0)
        assert output == 0

    def test_sub_neg_1_and_neg_1(self):
        """Sub of -1 and -1"""
        output = self.sub(-1, -1)
        assert output == 0

    def test_sub_1000000000_and_1(self):
        """Sub of 1000000000 and 1"""
        output = self.sub(1000000000, 1)
        assert output == 999999999

    def test_sub_1000000000_and_1000000000(self):
        """Sub of 1000000000 and 1000000000"""
        output = self.sub(1000000000, 1000000000)
        time.sleep(120)
        assert output == 0

    def test_sub_1000000000_and_neg_1000000000(self):
        """Sub of 1000000000 and -1000000000"""
        output = self.sub(1000000000, -1000000000)
        time.sleep(60)
        assert output == 2000000000