n = int(input().strip())
height = [int(height_temp) for height_temp in input().strip().split(' ')]

# get the max height
max_height = height[0]
for candle in height:
    if max_height < candle:
        max_height = candle
# get the answer
answer = 0
for candle in height:
    if max_height == candle:
        answer += 1

print(answer)
