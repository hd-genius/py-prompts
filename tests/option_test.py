import unittest
from unittest.mock import patch

from parameterized import parameterized

from pyprompts import options_prompt, PromptOption

class OptionsPromptTestCase(unittest.TestCase):
    @parameterized.expand([
        ['1', 'first value'],
        [' 1 ', 'first value'],
        ['2', 'second value'],
        [' 2 ', 'second value']
    ])
    def test_input_gives_expected_value(self, user_input, expected_result):
        with patch('builtins.input', return_value=user_input):
            result = options_prompt('Select a value', PromptOption('first', 'first value'), PromptOption('second', 'second value'))
            self.assertEqual(result, expected_result)

    @parameterized.expand([
        ['0'],
        ['-1']
    ])
    def test_input_before_beginning(self, user_input):
        with patch('builtins.input', side_effect=[user_input, 1]):
            with patch('builtins.print') as mock_print:
                options_prompt('Select a value', PromptOption('first', 'first value'), PromptOption('second', 'second value'))
                mock_print.assert_called_with('Please select an option between 1 and 2.')

    def test_input_beyond_end(self):
        with patch('builtins.input', side_effect=['3', 1]):
            with patch('builtins.print') as mock_print:
                options_prompt('Select a value', PromptOption('first', 'first value'), PromptOption('second', 'second value'))
                mock_print.assert_called_with('Please select an option between 1 and 2.')

    def test_input_not_number(self):
        with patch('builtins.input', side_effect=['other', 1]):
            with patch('builtins.print') as mock_print:
                options_prompt('Select a value', PromptOption('first', 'first value'), PromptOption('second', 'second value'))
                mock_print.assert_called_with('Please select an option between 1 and 2.')