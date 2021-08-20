def generate_sequence(number):
    while number != 1:
        if number % 2 == 0:
            number /= 2
        else:
            number = 3 * number + 1
        yield number
