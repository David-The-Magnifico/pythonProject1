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

    def test_fillD(self):
        SevenSegDisplay.fillD()
        self.assertEqual(SevenSegDisplay.segment, [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 0, 1]])

    def test_fillE(self):
        SevenSegDisplay.fillE()
        self.assertEqual(SevenSegDisplay.segment, [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]])

    def test_fillF(self):
        SevenSegDisplay.fillF()
        self.assertEqual(SevenSegDisplay.segment, [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]])

    def test_fillG(self):
        SevenSegDisplay.fillG()
        self.assertEqual(SevenSegDisplay.segment, [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 0]])

    def test_inputValue_valid(self):
        display = SevenSegDisplay()
        value = '1111111'
        display.inputValue(value)
        self.assertEqual(display.segment, [[1, 1, 1, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 1, 1, 1]])

