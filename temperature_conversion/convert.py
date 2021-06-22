def f_to_k(tf):
    """
    Convierte temperaturas de Fahrenheit a Kelvin

            Parameters:
                    tf : Temperatura en grados Fahrenheit

            Returns:
                    tk : Temperatura en grados Kelvin

    """

    tk = 273.5 + ((tf - 32.0) * (5.0 / 9.0))

    return tk


def c_to_r(tc):
    """
    Convierte temperaturas en Celsius a Rankine

            Parameters:
                    tc : Temperatura en grados Celsius

            Returns:
                    tr : Temperatura en grados Rankine
    """

    tr = (tc * 1.8) + 491.67

    return tr


def c_to_f(tc):
    """
    Convierte temperaturas en Celsius a Fahrenheit

            Parameters:
                    tc : Temperatura en grados Celsius

            Returns:
                    tf : Temperatura en grados Fahrenheit
    """

    tf = (tc * 1.8) + 32

    return tf
