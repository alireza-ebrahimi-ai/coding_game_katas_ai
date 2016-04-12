def next_version(version):
    all_parts = version.split(".")
    if len(all_parts) == 1:
        current_number = int(all_parts[0])
        return str(current_number + 1)

    max_item = len(all_parts) - 1
    all_parts[max_item] = str(int(all_parts[max_item]) + 1)
    if int(all_parts[max_item]) < 10:
        next_version_id = ''
        for index in range(len(all_parts)):
            next_version_id = next_version_id + all_parts[index]
            if (index != len(all_parts)-1):
               next_version_id += '.'
        return next_version_id

    if int(all_parts[max_item]) == 10:
        all_parts[max_item] = '0'
        all_parts[max_item - 1] = str(int(all_parts[max_item - 1]) + 1)

        move_it_move_it = True
        shifter = 1
        while move_it_move_it:

            if max_item - shifter != 0:
                if int(all_parts[max_item - shifter]) == 10:
                    all_parts[max_item - shifter] = '0'
                    all_parts[max_item - shifter - 1] = str(int(all_parts[max_item - shifter - 1]) + 1)
                    shifter += 1
                else:
                    move_it_move_it = False
            else:
                move_it_move_it = False

        next_version_id = ''
        for index in range(len(all_parts)):
            next_version_id = next_version_id + all_parts[index]
            if (index != len(all_parts)-1):
               next_version_id += '.'
        return next_version_id

