def get_trapezoid(upper=10, lower=10, height=10):
    return (upper + lower) * height / 2

print('台形の面積は', get_trapezoid(upper=2, height=3))
