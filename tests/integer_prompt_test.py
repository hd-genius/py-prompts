import unittest
from unittest.mock import patch

from parameterized import parameterized

from pyprompts import integer_prompt

class IntegerPromptTestCase(unittest.TestCase):
    def test_prompt_is_shown(self):
        with patch('builtins.input', return_value="1") as mock_input:
            prompt_text = 'Example integer prompt'
            integer_prompt(prompt_text)
            mock_input.assert_called_with(prompt_text)

    @parameterized.expand([
        ['0'],
        ['-1'],
        ['  4'],
        ['8  '],
    ])
    def test_prompt_accepts_integer(self, user_input):
        with patch('builtins.input', return_value=user_input):
            with patch('builtins.print') as mock_print:
                integer_prompt('Example integer prompt')
                mock_print.assert_not_called()

    @parameterized.expand([
        ['O'],
        ['3.14'],
        ['inf']
    ])
    def test_prompt_does_not_accept(self, user_input):
        with patch('builtins.input', side_effect=(user_input, "1")):
            with patch('builtins.print') as mock_print:
                integer_prompt('Example integer prompt')
                mock_print.assert_called_with('The value is not a valid integer. Please enter an integer.')

if __name__ == '__main__':
    unittest.main()