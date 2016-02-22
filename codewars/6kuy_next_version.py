def next_version(version):
    all_parts = version.split(".")
    if len(all_parts) == 1:
        current_number = int(all_parts[0])
        return str(current_number + 1)

    int_version = ''
    for index in range(len(all_parts)):
        int_version += all_parts[index]

    int_version = str(int(int_version) + 1)

    new_version = ''


    return int_version

print next_version("0.1")
