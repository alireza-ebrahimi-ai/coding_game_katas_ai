def read_genome(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            if not line[0] == '>':
                genome += line.rstrip()
    return genome

def readFastq(filename):
    sequences = []
    qualities = []
    with open(filename) as fh:
        fh.readline()
        seq = fh.readline().rstrip()
        fh.readline()
        qual = fh.readline().rstrip()
        if len(seq) == 0:
            break
        sequences.append(seq)
        qualities.append(qual)
    return sequences, qualities


