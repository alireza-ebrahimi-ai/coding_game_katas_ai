import re

def parse_fen(string):
    symbols = {'P': u'\u2659', 'N': u'\u2658', 'B': u'\u2657', 'R': u'\u2656',
               'Q': u'\u2655', 'K': u'\u2654',
               'p': u'\u265F', 'n': u'\u265E', 'b': u'\u265D', 'r': u'\u265C',
               'q': u'\u265B', 'k': u'\u265A'}

    color_table = {'11': u'\uff3f', '12': u'\u2587', '13': u'\uff3f', '14': u'\u2587', '15': u'\uff3f', '16': u'\u2587', '17': u'\uff3f', '18': u'\u2587',
                   '21': u'\u2587', '22': u'\uff3f', '23': u'\u2587', '24': u'\uff3f', '25': u'\u2587', '26': u'\uff3f', '27': u'\u2587', '28': u'\uff3f',
                   '31': u'\uff3f', '32': u'\u2587', '33': u'\uff3f', '34': u'\u2587', '35': u'\uff3f', '36': u'\u2587', '37': u'\uff3f', '38': u'\u2587',
                   '41': u'\u2587', '42': u'\uff3f', '43': u'\u2587', '44': u'\uff3f', '45': u'\u2587', '46': u'\uff3f', '47': u'\u2587', '48': u'\uff3f',
                   '51': u'\uff3f', '52': u'\u2587', '53': u'\uff3f', '54': u'\u2587', '55': u'\uff3f', '56': u'\u2587', '57': u'\uff3f', '58': u'\u2587',
                   '61': u'\u2587', '62': u'\uff3f', '63': u'\u2587', '64': u'\uff3f', '65': u'\u2587', '66': u'\uff3f', '67': u'\u2587', '68': u'\uff3f',
                   '71': u'\uff3f', '72': u'\u2587', '73': u'\uff3f', '74': u'\u2587', '75': u'\uff3f', '76': u'\u2587', '77': u'\uff3f', '78': u'\u2587',
                   '81': u'\u2587', '82': u'\uff3f', '83': u'\u2587', '84': u'\uff3f', '85': u'\u2587', '86': u'\uff3f', '87': u'\u2587', '88': u'\uff3f',}

    args = string.split(' ')
    rows = args[0].split('/')

   # rows = list(reversed(rows))

    answer = ''

    horizontal_index = 9
    for row in rows:
        output = ''
        horizontal_index -= 1
        vertical_index = 1
        for position in xrange(0, len(row)):

            if not (re.match(r'[1-8]', row[position]) is None):

            #empty squares fill
                for plot in range(0, int(row[position])):
                    if args[1] == 'w':
                        output = output + color_table[str(horizontal_index) + str(vertical_index)]
                    else:
                        if color_table[str(horizontal_index) + str(vertical_index)] == u'\uff3f':
                            output = output + u'\u2587'
                        else:
                            output = output + u'\uff3f'

                    vertical_index += 1
            #figures fill
            else:
                output = output + symbols[row[position]]
                vertical_index += 1

        answer = answer + unicode(output) + '\n'
    return unicode(answer)

