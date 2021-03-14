def check_int(number):
    if number.isdigit() is False:
        return False
    return True


def check_float(number):
    try:
        float(number)
    except ValueError:
        return False
    return True


def check_positive(number):
    if number < 0:
        return False
    return True


def validate_int(number):
    while check_int(number) is False:
        number = input()
    return int(number)


def validate_digit(number):
    while check_int(number) is False:
        number = input()
    return number


def validate_id(number,test_list):
    if number in test_list:
        return False
    return True



