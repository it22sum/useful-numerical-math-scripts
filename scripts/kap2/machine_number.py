def machine_number(value, exponent=8,mantissa=23):
    """
    Diese Funktion berechnet die Maschinenzahl einer Dezimalzahl. \n
    Die Defaultwerte für Exponent und Mantisse sind 8 und 23.\n
    Nach IEEE 754 Standard: \n
    Einzelgenauigkeit (single Precision): 32 Bit (1 Bit Vorzeichen, 8 Bit Exponent, 23 Bit Mantisse) \n
    Doppelgenauigkeit (double Precision): 64 Bit (1 Bit Vorzeichen, 11 Bit Exponent, 52 Bit Mantisse) \n

    :param value: Die Zahl, die in eine Maschinenzahl umgewandelt werden soll.
    :param exponent: Exponent der Maschinenzahl
    :param mantissa: Mantisse der Maschinenzahl
    :return: Vorzeichen, Exponent, Mantisse, Ergebnis als String
    """

    #Vorzeichen berechnen
    if value > 0:
        sign = '0'
    else:
        sign = '1'

    #Bias berechnen
    bias = 2**(exponent-1)-1

    #Vorkommastellen berechnen
    integerValue = abs(int(value))
    binaryIntegerValue = bin(integerValue)[2:]

    #Exponent berechnen
    binaryIntegerValueExponent = len(binaryIntegerValue)-1

    #Nachkommastellen berechnen
    fractionalValue = abs(value) - abs(integerValue)
    binaryFractionalValue = convert_fraction_to_binary(fractionalValue)

    #Mantisse berechnen
    mantissaValue = binaryIntegerValue[1:] + binaryFractionalValue
    correctMantissaLength = mantissaValue[:mantissa]
    if len(correctMantissaLength) < mantissa:
        correctMantissaLength = correctMantissaLength + '0'*(mantissa-len(correctMantissaLength))

    #bias berechnen
    biasValue = bin(binaryIntegerValueExponent + bias)[2:]

    #Ergebnis als String zusammenfassen
    strResult = str("Vorzeichen (0 Positiv, 1 Negative): " + sign + "\n"
                 + "Exponent: " + biasValue + "\n"
                 + "Mantisse inklusive führende 1: 1." + correctMantissaLength + "\n"
                 + "|" + sign + "|" + biasValue + "|" + correctMantissaLength + "|")


    #Ergebnis
    return sign, biasValue, correctMantissaLength, strResult

def convert_fraction_to_binary(fraction):
    """ Convert the fractional part of a decimal number to binary. """
    binary = ''
    while fraction and len(binary) < 64:  # Limit to 64 iterations
        fraction *= 2
        if fraction >= 1:
            binary += '1'
            fraction -= 1
        else:
            binary += '0'
    return binary


if __name__ == '__main__':
    result_machine_number = machine_number(value=3.5)
    print(result_machine_number[0])
    print(result_machine_number[1])
    print(result_machine_number[2])
    print(result_machine_number[3])
