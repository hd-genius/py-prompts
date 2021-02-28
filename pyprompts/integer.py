from pyprompts._prompt import prompt
from pyprompts._utilities import is_integer

def integer_prompt(prompt_text: str) -> int:
    return prompt(prompt_text, is_integer, 'The value is not a valid integer. Please enter and integer.', int)
