from src.kuy6.rna_to_protein_sequence_translation import protein


def test_simple_case():
    assert protein('AUG') == 'M'

def test_complex_case():
    assert protein('AUGCUAUGGAGGGUAGUGUUAACUACCACGCCCAGUACUUGA') == 'MLWRVVLTTTPST'


