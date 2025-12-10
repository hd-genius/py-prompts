import unittest
from unittest.mock import patch

from parameterized import parameterized
from pyprompts import confirmation_prompt

class ConfirmationPromptTestCase(unittest.TestCase):
    def test_prompt_is_shown(self):
        with patch('builtins.input', return_value="yes") as mock_input:
            prompt_text = 'Example confirmation prompt'
            confirmation_prompt(prompt_text)
            mock_input.assert_called_with(prompt_text + '((Y)es/(N)o)')

    @parameterized.expand([
        ['Y'],
        [' Y '],
        ['y'],
        [' y '],
        ['YES'],
        [' YES '],
        ['yes'],
        [' yes '],
        ['yEs'],
        [' yEs ']
    ])
    def test_affirmative_response(self, user_input):
        with patch('builtins.input', return_value=user_input):
            result = confirmation_prompt('Example confirmation prompt')
            self.assertTrue(result)

    @parameterized.expand([
        ['N'],
        [' N '],
        ['n'],
        [' n '],
        ['NO'],
        [' NO '],
        ['no'],
        [' no '],
        ['nO'],
        [' nO ']
    ])
    def test_negative_response(self, user_input):
        with patch('builtins.input', return_value=user_input):
            result = confirmation_prompt('Example confirmation prompt')
            self.assertFalse(result)
    
    @parameterized.expand([
        ['on'],
        ['es'],
        ['non'],
        ['other'],
        [' '],
        ['']
    ])
    def test_invalid_response(self, user_input):
        expected_error_message = 'The user input was not a valid option. Please select either (Y)es or (N)o.'
        with patch('builtins.input', side_effect=(user_input, "yes")):
            with patch('builtins.print') as mock_print:
                prompt_text = 'Example confirmation prompt'
                confirmation_prompt(prompt_text)
                mock_print.assert_called_with(expected_error_message)

if __name__ == '__main__':
    unittest.main()