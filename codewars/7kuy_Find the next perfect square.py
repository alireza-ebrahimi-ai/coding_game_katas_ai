import math
def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    if math.sqrt(sq) % 1 != 0:
      return -1
    if math.sqrt(sq) % 1 == 0:
      return (math.sqrt(sq) + 1) * (math.sqrt(sq) + 1)