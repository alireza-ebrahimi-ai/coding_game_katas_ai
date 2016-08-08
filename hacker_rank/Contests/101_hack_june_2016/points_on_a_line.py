n = int(input().strip())
line_x = []
line_y = []
x_line = True
y_line = True
for a0 in range(n):
    x,y = input().strip().split(' ')
    line_x.append(x)
    line_y.append(y)

for i in range(0, n - 1):
    if line_x[i] != line_x[i + 1]:
        x_line = False
    if line_y[i] != line_y[i + 1]:
        y_line = False

if x_line or y_line:
    print("YES")
else:
    print("NO")




