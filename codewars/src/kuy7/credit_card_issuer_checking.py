def get_issuer(number):
    code = str(number)
    if len(code) < 13 or len(code) > 16:
        return 'Unknown'
    if len(code) == 15 and (code[0:2] == '37' or code[0:2] == '34'):
        return 'AMEX'
    if len(code) == 16 and code[0:4] == '6011':
        return 'Discover'
    if (len(code) == 16 or len(code) == 13) and code[0] == '4':
        return 'VISA'
    if (len(code) == 16 and ((code[0:2] == '51') or (code[0:2] == '52') or (code[0:2] == '53') or (code[0:2] == '54') or (code[0:2] == '55'))):
        return 'Mastercard'
    return 'Unknown'

