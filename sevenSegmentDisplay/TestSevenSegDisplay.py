import unittest

from SevenSegDisplay import SevenSegDisplay


class TestSevenSegDisplay(unittest.TestCase):

    def test_fillA(self):
        SevenSegDisplay.fillA()
        self.assertEqual(SevenSegDisplay.segment, [[1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])

 def test_fillB(self):
        SevenSegDisplay.fillB()
        self.assertEqual(SevenSegDisplay.segment, [[0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0]])

    def test_fillC(self):
        SevenSegDisplay.fillC()
        self.assertEqual(SevenSegDisplay.segment, [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 0]])

