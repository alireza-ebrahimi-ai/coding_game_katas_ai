def get_reversed_color(hex_color):
    if hex_color == "":
        return "#" + "FFFFFF"
    if len(hex_color) > 6:
        raise ValueError("Invalid length value")

    contr_int_color = 16777215 - int(hex_color, 16)
    contr_int_color = str(hex(contr_int_color))[2:]

    if len(contr_int_color) < 6:
        for i in range(0, 6 - len(contr_int_color)):
            contr_int_color = "0" + contr_int_color

    format_hex = "#" + contr_int_color

    return format_hex.upper()
