from pyprompts._prompt import prompt

_affirmative_responses = ("y", "yes")
_affirmative_response = "(Y)es"
_negative_responses = ("n", "no")
_negative_response = "(N)o"


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
    invalid_message = f'The user input was not a valid option. Please select either {_affirmative_response} or {_negative_response}.'

    return prompt(prompt_text + f'({_affirmative_response}/{_negative_response})', _check_input_validity, invalid_message, _is_affirmative)
