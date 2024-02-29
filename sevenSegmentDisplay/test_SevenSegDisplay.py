import pytest

from SevenSegDisplay import SevenSegDisplay


class TestSevenSegDisplay:
    def test_input_value_valid(self):
        display = SevenSegDisplay()
        value = '0110000'
        display.inputValue(value)
        assert display.segment == [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    def test_input_value_invalid_length(self):
        display = SevenSegDisplay()
        value = '011000000'
        with pytest.raises(ValueError):
            display.inputValue(value)

    def test_input_value_invalid_character(self):
        display = SevenSegDisplay()
        value = '0110000a'
        with pytest.raises(ValueError):
            display.inputValue(value)
