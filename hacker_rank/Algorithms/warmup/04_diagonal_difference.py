n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

primary_diagonal = 0
secondary_diagonal = 0

for i in range(0, n):
    primary_diagonal = primary_diagonal + a[i][i]

for k in range(0, n):
    secondary_diagonal = secondary_diagonal + a[n - k - 1][k]

print(abs(primary_diagonal - secondary_diagonal))