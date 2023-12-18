def konditionszahl(f, x):
    from sympy import symbols, diff
    x_symbol = symbols('x')
    derivative = diff(f, x_symbol)

    f_value = f.subs(x_symbol, x)
    derivative_value = derivative.subs(x_symbol, x)

    return (abs(derivative_value) * abs(x)) / abs(f_value)
