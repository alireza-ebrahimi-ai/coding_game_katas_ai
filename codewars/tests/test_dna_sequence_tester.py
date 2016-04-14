import pytest
from src.kuy6.dna_sequence_tester import check_DNA


@pytest.mark.skip(reason='unused test')
def test_reverse():
    assert check_DNA('ATGC', 'ATGC') == 'CGTA'


@pytest.mark.skip(reason='unused test')
def test_check_decoding():
    assert check_DNA('AAAA', 'ATGC') == 'GCAT'


def test_1():
    assert check_DNA('AAAA', 'TTTT') == True

def test_2():
    assert check_DNA('GTCTTAGTGTAGCTATGCATGC', 'GCATGCATAGCTACACTACGAC') == False

def test_3():
    assert check_DNA('CGATACGAACCCATAATCG', 'CTACACCGGCCGATTATGG') == False

def test_4():
    assert check_DNA('GCGCTGCTAGCTGATCGA', 'ACGTACGATCGATCAGCTAGCAGCGCTAC') == True

def test_5():
    assert check_DNA('GTCACCGA', 'TCGGCTGAC') == False

def test_6():
    assert check_DNA('TAATACCCGACTAATTCCCC', 'GGGGAATTTCGGGTATTA') == False



