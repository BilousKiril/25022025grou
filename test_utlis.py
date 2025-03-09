from utlis import add_two_numbers
import pytest


class TestAddTwoNumbers:

    def test_add_two_numbers_success(self):
        number1 = 2
        number3 = 3
        expected_result = 5
        actual_result = add_two_numbers(number1, number3)
        assert actual_result == expected_result, "fix "

    def test_add_two_strings_success(self):
        number1 = '221'
        number3 = '221'
        expected_result = 442
        actual_result = add_two_numbers(number1, number3)
        assert actual_result == expected_result, "fix "


    def test_add_two_strings_fall(self):
        number1 = 'gsgsg'
        number3 = 'gsgs'
        with pytest.raises(ValueError):
            add_two_numbers(number1, number3)

