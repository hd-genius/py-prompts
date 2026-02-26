def prompt(prompt_text: str, is_valid_input, invalid_selection_message: str, result_converter):
    while True:
        user_input = input(prompt_text)
        if is_valid_input(user_input):
            return result_converter(user_input)
        print(invalid_selection_message)
