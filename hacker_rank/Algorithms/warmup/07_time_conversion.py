time = input().strip()

if time == '12:00:00PM':
    print('12:00:00')
    exit()
if time == '12:00:00AM':
    print('00:00:00')
    exit()

if time[-2:] == 'PM':
    if time[0:2] != '12':
        print(str(int(time[:2]) + 12) + time[2:-2])
    else:
        print(str(int(time[:2])) + time[2:-2])


elif time[-2:] == 'AM':
    if time[0:2] != '12':
        print('0' + str(int(time[:2])) + time[2:-2])
    else:
        print('0' + str(int(time[:2]) - 12) + time[2:-2])
