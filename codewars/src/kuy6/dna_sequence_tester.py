def check_DNA(seq1, seq2):
    binom = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    seq2_redirected = seq2[::-1]
    decoded_seq2 = ''
    for i in range(0, len(seq2)):
        decoded_seq2 += binom[seq2_redirected[i]]
    if (seq1 in decoded_seq2) or (decoded_seq2 in seq1):
        return True
    return False
















