def is_integer(value: str):
    try:
        int(value)
        return True
    except ValueError:
        return False
