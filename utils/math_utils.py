import math


def solve_quiz(alert_text):
    x = alert_text.split(" ")[2]
    answer = str(math.log(abs((12 * math.sin(float(x))))))
    return answer


def click_real_url():
    math_value = str(math.ceil(math.pow(math.pi, math.e) * 10000))
    return math_value
