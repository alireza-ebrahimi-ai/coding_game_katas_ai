from src.kuy7.credit_card_issuer_checking import get_issuer


def test_zero():
    assert get_issuer(0) == 'Unknown'
    assert get_issuer(123456) == 'Unknown'
    assert get_issuer(378282246310005111) == 'Unknown'

def test_AMEX():
    assert get_issuer(378282246310005) == 'AMEX'
    assert get_issuer(348282246310005) == 'AMEX'

def test_discover():
    assert get_issuer(6011822463100051) == 'Discover'

def test_VISA():
    assert get_issuer(4011822463100051) == 'VISA'

def test_Mastercard():
    assert get_issuer(5111822463100051) == 'Mastercard'
    assert get_issuer(5211822463100051) == 'Mastercard'
    assert get_issuer(5311822463100051) == 'Mastercard'
    assert get_issuer(5511822463100051) == 'Mastercard'
