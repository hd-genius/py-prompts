from pyprompts._prompt import prompt

affirmative_responses = ("y", "yes")
affirmative_response = "(Y)es"
negative_responses = ("n", "no")
negative_response = "(N)o"

def confirmation_prompt(prompt_text: str) -> bool:
    invalid_message = f'The user input was not a valid option. Please select either {affirmative_response} or {negative_response}.'

    def is_affirmative(response: str) -> bool:
        return response.strip().lower() in affirmative_responses

    def is_negative(response: str) -> bool:
        return negative_responses.lower() == response.lower()

    def validity_check(response: str) -> bool:
        return is_affirmative(response) or is_negative(response)

    return prompt(prompt_text + f'({affirmative_response}/{negative_response})', validity_check, invalid_message, is_affirmative)