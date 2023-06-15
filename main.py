def get_value_of_polynomial(value: str, x: str) -> int:
    coefficients = value.split()

    coefficients = [int(coefficient) for coefficient in coefficients]

    result = 0
    power = len(coefficients) - 1

    for coefficient in coefficients:
        result += coefficient * (int(x) ** power)
        power -= 1

    return result


get_value_of_polynomial("10 10 10 10 10", "2")
