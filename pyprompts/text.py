from pyprompts._prompt import prompt

def text_prompt(prompt_text: str):
    return prompt(prompt_text, lambda x: True, '', lambda x: x)
