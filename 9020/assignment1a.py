from random import seed, shuffle


def generate_dial_and_centre(for_seed):
    global dir, d , base_number
    d = {'S': 0, 'H': 1, 'D': 2, 'C': 3}
    base_number = 127136
    dir = dict.fromkeys(str(i) for i in range(1, 11))
    for i in dir.keys():
        dir[i] = int(i)
    dir['j'] = 11
    dir['q'] = 13
    dir['k'] = 14
    colours = 'CDHS'  # Clubs, Diamonds, Hearts, Spades
    #                                            jacks, queens, kings
    ranks = list(str(x) for x in range(1, 11)) + list('jqk')
    seed(for_seed)
    cards = [colour + rank for colour in colours for rank in ranks]
    shuffle(cards)
    dial = dict.fromkeys(range(1, 13))
    for i in range(12):
        dial[i + 1] = [cards[i + 13 * j] for j in range(4)]
    return dial, [cards[12 + 13 * j] for j in range(4)]


def initial_hour(hour, dial):
    print('  '.join(f'hidden{chr(d[dial[hour][i][0]] * 16 + dir[dial[hour][i][1:]] + base_number)}'
                    for i in range(len(dial[hour]))))
    # REPLACE PASS ABOVE WITH YOUR CODE


def hour_after_playing_from_beginning_for_at_most(hour, nb_of_steps, dial,
                                                  centre
                                                  ):
    dial[13] = centre
    current_hour = 13
    state_of_stacks = [0] * 13
    counter = 0
    while counter < nb_of_steps and state_of_stacks[current_hour - 1] != len(dial[current_hour]):
        card = dial[current_hour].pop()
        next_hour = dir[card[1:]]
        if next_hour > 11:
            next_hour -= 1
        dial[next_hour].insert(0,card)
        state_of_stacks[next_hour - 1] += 1
        current_hour = next_hour
        counter += 1
    if counter < nb_of_steps and counter != 52:
        if hour != -1:
            print('Could not play that far...')
        return False
    else:
        if hour != -1:
            print(state_of_stacks[hour - 1])
            for i in range(len(dial[hour])):
                f = d[dial[hour][i][0]] * 16
                c = dir[dial[hour][i][1:]]
                if state_of_stacks[hour-1] > i:
                    print(chr(f + c + base_number), end='')
                else:
                    print(f'hidden{chr(f + c + base_number)}', end='')
                if i != len(dial[hour]) - 1:
                    print('  ', end='')
            print()
        return True
    # REPLACE PRINT() ABOVE WITH YOUR CODE


def kings_at_end_of_game(dial, centre):
    flag = hour_after_playing_from_beginning_for_at_most(-1, 52, dial, centre)
    if not flag:
        print('No success...')
    else:
        hour = 13
        print('  '.join(chr(d[dial[hour][i][0]] * 16 + dir[dial[hour][i][1:]] + base_number)
                        for i in range(len(dial[hour]))))
    # REPLACE PRINT() ABOVE WITH YOUR CODE


# POSSIBLY DEFINE OTHER FUNCTIONS
# dial, centre = generate_dial_and_centre(18)
# hour_after_playing_from_beginning_for_at_most(10, 2, dial, centre)
#kings_at_end_of_game(dial, centre)
# for hour in dial:
#    print(f'{hour:2}', dial[hour], sep=': ')
#nitial_hour(10, dial)