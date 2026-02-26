from collections import namedtuple
from functools import reduce
from pyprompts._prompt import prompt
from pyprompts._utilities import is_integer

PromptOption = namedtuple('PromptOption', ['description', 'value'])


def options_prompt(prompt_text: str, *options: PromptOption):
    options_text = [_format_option_text(
        index + 1, x.description) for index, x in enumerate(options)]
    presented_prompt = reduce(
        lambda a, b: a + b, options_text, prompt_text + '\n')

    def index_of_selection(value: str):
        return int(value) - 1

    def is_valid_option(value: str):
        if not is_integer(value):
            return False
        selected_option = index_of_selection(value)
        return 0 <= selected_option < len(options)

    def find_selected_value(value: str):
        selected_option = options[index_of_selection(value)]
        return selected_option.value

    return prompt(presented_prompt,
                  is_valid_option,
                  f'Please select an option between 1 and {len(options)}.',
                  find_selected_value)


def _format_option_text(option_number: int, description: str):
    return f'{option_number}: {description}\n'
