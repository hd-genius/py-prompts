from pyprompts._prompt import prompt

_affirmative_responses = ("y", "yes")
_AFFIRMATIVE_RESPONSE = "(Y)es"
_negative_responses = ("n", "no")
_NEGATIVE_RESPONSE = "(N)o"


def _is_affirmative(response: str) -> bool:
    return response.strip().lower() in _affirmative_responses


def _is_negative(response: str) -> bool:
    return response.strip().lower() in _negative_responses


def _check_input_validity(response: str) -> bool:
    return _is_affirmative(response) or _is_negative(response)


def confirmation_prompt(prompt_text: str) -> bool:
    """Presents a prompt to the user that ask for an affirmative (yes) or negative (no) response.
    If the user responds "yes" the function returns True.
    If the user responds "no" the function returns False."""
    invalid_message = ('The user input was not a valid option. Please select either '
                       f'{_AFFIRMATIVE_RESPONSE} or {_NEGATIVE_RESPONSE}.')

    return prompt(prompt_text + f'({_AFFIRMATIVE_RESPONSE}/{_NEGATIVE_RESPONSE})',
                  _check_input_validity,
                  invalid_message,
                  _is_affirmative)
