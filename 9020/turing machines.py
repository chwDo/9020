instructions = {}
with open('division_by_2.txt') as x:
    for line in x:
        if line.isspace() or line.startswith('#'):
            continue
        state, bit, new_state, new_bit, direction = line.split()
        instructions[state, int(bit)] = \
            new_state, int(new_bit), direction
tape = [0, 0] + [1] * 7 + [0, 0] * 3
current_state = 'del1'
current_position = tape.index(1)
current_bit = tape[current_position]

while (current_state, current_bit) in instructions:
    new_state, new_bit, direction = instructions[current_state, current_bit]
    tape[current_position] = new_bit
    current_state = new_state
    if direction == 'R':
        current_position += 1
    else:
        current_position -= 1
    current_bit = tape[current_position]
print(tape)
