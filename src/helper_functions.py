def format_number(num):
    if isinstance(num, float) and num == int(num):
        return str(int(num))
    return str(num)
