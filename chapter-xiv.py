def miu_char_to_godel_digit(char):
    if char == "M":
        return 3

    if char == "I":
        return 1

    return 0

def godel_digit_to_miu_char(digit):
    if digit == 3:
        return "M"

    if digit == 1:
        return "I"

    return "U"

def miu_to_godel_number(lines):
    godel_number = 0

    for line in lines:
        for char in line:
            godel_number *= 10
            godel_number += miu_char_to_godel_digit(char)

    return godel_number

def godel_number_to_miu(godel_number):
    lines = []
    line = ""

    while godel_number > 0:
        digit = godel_number % 10
        char = godel_digit_to_miu_char(digit)

        line = char + line

        # First character of line reached. Start a new line.
        if char == "M":
            lines.insert(0, line)
            line = ""

        godel_number -= digit
        godel_number /= 10

    return lines

#miu_to_godel_number(["MI", "MII", "MIII", "MUI"])
#godel_number_to_miu(313113111301)
#godel_number_to_miu(miu_to_godel_number(["MI", "MII", "MIII", "MUI"]))
