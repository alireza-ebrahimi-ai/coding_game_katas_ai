import math
def am_i_wilson(n):
    if n < 2:
      return False
    elif (math.factorial(n-1) + 1) / (n * n) == 1:
	  return True
    else:
	  return False

print am_i_wilson(3)