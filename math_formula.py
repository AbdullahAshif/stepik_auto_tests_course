import math


def formula_to_math(x):
    value = 12 * math.sin(x)
    abs_value = abs(value)
    ln_value = math.log(abs_value)
    return ln_value
