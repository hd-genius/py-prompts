from functools import reduce
from pyprompts._prompt import prompt
from pyprompts._utilities import is_integer

def options_prompt(prompt_text: str, *options):
    options_text = [_format_option_text(index + 1, x[0], index < len(options) - 1) for index, x in enumerate(options)]
    presented_prompt = reduce(lambda a, b: a + b, options_text, prompt_text + '\n')

    def is_valid_option(value: str):
        if (not is_integer(value)):
            return False
        selected_option = index_of_selection(value)
        return selected_option >= 0 and selected_option < len(options)
            

    def find_selected_option(value: str):
        selected_option = options[index_of_selection(value)]
        return selected_option[1]

    def index_of_selection(value: str):
        return int(value) - 1

    return prompt(presented_prompt, is_valid_option, f'please select an option between 1 and {len(options)}', find_selected_option)

def create_option(description: str, value):
    return (description, value)

def _format_option_text(option_number: int, description: str, is_last: bool):
    return f'{option_number}: {description}\n'
