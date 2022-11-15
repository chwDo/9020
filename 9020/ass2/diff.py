# Insert your code in this file
from collections import defaultdict
from itertools import combinations
import re

class DiffCommandsError(Exception):
    pass


class DiffCommands:
    def __init__(self, text_name):
        file1 = open(text_name, 'r')
        self.lines = file1.readlines()
        file1.close()
        if not self.verdict():
            raise DiffCommandsError('Cannot possibly be the commands for the diff of two files')

    def verdict(self):
        flag = True
        if '\n' in self.lines:
            flag = False
        flag_2 = False  # represent whether a,d,c arise in command
        index_1, index_2, offset = [0, 0], [0, 0], 0
        for i in self.lines:
            count = 0
            for ii in i:
                if ii.isalpha():
                    count += 1
            if count != 1:
                return False
            i = i.strip('\n')
            if ' ' in i:
                return False
            if 'd' in i:
                if i.count(',') == 2:
                    return False
                flag_2 = True
                subcommand = i.split('d')
                if subcommand[0].count(',') == 0:  # if only delete one line
                    index_1[1] = int(subcommand[0])
                    offset -= 1
                else:
                    l1 = int(subcommand[0].split(',')[0])
                    l2 = int(subcommand[0].split(',')[1])
                    if l2 <= l1:  # the second number must great than first
                        return False
                    index_1[1] = l2
                    offset -= l2 - l1 + 1  # record lines' change
                r1 = r2 = int(subcommand[1])
                index_2[1] = r2  # There is only one number in right side
                if (index_1[1] + offset) != index_2[1]:
                    return False
                index_1[0], index_2[0] = index_1[1], index_2[1]
            if 'a' in i:
                if i.count(',') == 2:
                    return False
                flag_2 = True
                subcommand = i.split('a')
                if subcommand[1].count(',') == 0:  # if only add one line
                    index_2[1] = int(subcommand[1])
                    offset += 1
                else:
                    r1 = int(subcommand[1].split(',')[0])
                    r2 = int(subcommand[1].split(',')[1])
                    if r2 <= r1:  # the second number must great than first
                        return False
                    index_2[1] = r2
                    offset += r2 - r1 + 1
                l1 = l2 = int(subcommand[0])
                index_1[1] = l2
                if (index_1[1] + offset) != index_2[1]:
                    return False
                index_1[0], index_2[0] = index_1[1], index_2[1]

            if 'c' in i:
                flag_2 = True
                subcommand = i.split('c')
                if subcommand[0].count(','):
                    l1 = int(subcommand[0].split(',')[0])
                    l2 = int(subcommand[0].split(',')[1])
                    if l2 <= l1:  # the second number must great than first
                        return False
                else:
                    l1 = l2 = int(subcommand[0])
                if subcommand[1].count(','):
                    r1 = int(subcommand[1].split(',')[0])
                    r2 = int(subcommand[1].split(',')[1])
                    if r2 <= r1:  # the second number must great than first
                        print(r2, r1)
                        return False
                else:
                    r1 = r2 = int(subcommand[1])
                index_1[1] = l2
                index_2[1] = r2
                # should have gap between change and last operation
                if l1 - index_1[0] == 1 or r2 - index_2[0] == 1:
                    return False
                offset += (r2 - r1) - (l2 - l1)
                if (index_1[1] + offset) != index_2[1]:
                    return False
                index_1[0], index_2[0] = index_1[1], index_2[1]
            if not flag_2:
                return False
        return flag

    def __str__(self):
        str = ''.join(self.lines)
        return str[:-1]


class OriginalNewFiles:
    def __init__(self, file_1, file_2):
        file1 = open(file_1, 'r')
        self.lines_1 = file1.readlines()
        file1.close()
        file2 = open(file_2, 'r')
        self.lines_2 = file2.readlines()
        self.output = ['chw']
        self.output_unmodified_original = ['chw']
        self.output_unmodified_new = ['chw']

    def is_a_possible_diff(self, diff):
        for i in 'acd':
            if i in diff.lines[-1]:
                commands = diff.lines[-1].split(i)[1].strip('\n')
        if commands.count(',') == 0:
            length = int(commands)
        else:
            length = int(commands.split(',')[1])
        if len(self.lines_2) < length:
            return False
        else:
            self._get_answer_arrays(diff)
            answer_original = []
            answer_new = []
            for i in self.output_unmodified_original:
                if i != '...':
                    answer_original.append(i)
            for i in self.output_unmodified_new:
                if i != '...':
                    answer_new.append(i)
            if len(answer_new) == len(answer_original):
                return True
            else:
                return False

    # def _caculate(self, diff_list, flag, position, lines, return_j):
    #     line = [1] * (len(lines) + 1)
    #     for i in diff_list.obj_list:
    #         if flag:
    #             hind_lines_num = re.split(r'[dc]', i)
    #         else:
    #             hind_lines_num = re.split(r'[ac]', i)
    #         str = 'a' if flag else 'd'
    #         if str not in hind_lines_num[0]:
    #             if ',' in hind_lines_num[position]:
    #                 if int(hind_lines_num[position].split(',')[1]) >= len(line):
    #                     return False
    #                 for j in range(int(hind_lines_num[position].split(',')[0]),
    #                                int(hind_lines_num[position].split(',')[1]) + 1):
    #                     line[j] = 0
    #             else:
    #                 if int(hind_lines_num[position]) >= len(line):
    #                     return False
    #                 line[int(hind_lines_num[position])] = 0
    #     display_lines = [i for i in range(0, len(line)) if line[i]]
    #     if return_j == 1:
    #         for i, j in zip(display_lines, display_lines[1:]):
    #             if j - i != 1:
    #                 print('...')
    #             print(lines[j - 1].strip('\n'))
    #         if display_lines[-1] < len(lines):
    #             print('...')
    #     else:
    #         return display_lines
    #
    # def output_unmodified_from_original(self, diff_list):
    #     self._caculate(diff_list, True, 0, self.object_1, 1)
    #
    # def output_unmodified_from_new(self, diff_list):
    #     self._caculate(diff_list, False, 1, self.object_2, 1)

    def _get_answer_arrays(self, diff):
        output = []
        output_unmodified_original = []
        output_unmodified_new = []
        index_1, index_2, offset = [0, 0], [0, 0], 0
        for i in diff.lines:
            line = i.strip('\n')
            output.append(line)
            if 'd' in line:
                subcommands = line.split('d')
                if subcommands[0].count(',') == 0:  # if only delete one line
                    l1 = l2 = int(subcommands[0])
                else:
                    l1 = int(subcommands[0].split(',')[0])
                    l2 = int(subcommands[0].split(',')[1])
                    # print(index_1, index_2, offset)
                r1 = r2 = int(subcommands[1])
                l1 -= 1
                for ii in range(l1, l2):
                    output.append('< ' + self.lines_1[ii].strip('\n'))
                offset = 0
                offset_new = 0

            if 'a' in line:
                subcommands = line.split('a')
                if subcommands[1].count(',') == 0:  # if only add one line
                    r1 = r2 = int(subcommands[1])
                else:
                    r1 = int(subcommands[1].split(',')[0])
                    r2 = int(subcommands[1].split(',')[1])
                l1 = l2 = int(subcommands[0])
                r1 -= 1
                for ii in range(r1, r2):
                    output.append('> ' + self.lines_2[ii].strip('\n'))
                offset = -1
                offset_new = -1

            if 'c' in line:
                subcommands = line.split('c')
                if subcommands[0].count(','):
                    l1 = int(subcommands[0].split(',')[0])
                    l2 = int(subcommands[0].split(',')[1])
                else:
                    l1 = l2 = int(subcommands[0])

                if subcommands[1].count(','):
                    r1 = int(subcommands[1].split(',')[0])
                    r2 = int(subcommands[1].split(',')[1])
                else:
                    r1 = r2 = int(subcommands[1])
                l1 -= 1
                r1 -= 1
                for ii in range(l1, l2):
                    output.append('< ' + self.lines_1[ii].strip('\n'))
                output.append('---')
                for ii in range(r1, r2):
                    output.append('> ' + self.lines_2[ii].strip('\n'))
                offset = 0
                offset_new = -1

            index_1[1] = l1
            if index_1[1] - index_1[0] > 0:
                for ii in range(index_1[0], index_1[1]):
                    output_unmodified_original.append(self.lines_1[ii].strip('\n'))
            if offset == 0:
                output_unmodified_original.append('...')
            index_1[0] = l2
            index_2[1] = r1
            if index_2[1] - index_2[0] > 0:
                for ii in range(index_2[0], index_2[1]):
                    output_unmodified_new.append(self.lines_2[ii].strip('\n'))
            if offset_new != 0:
                output_unmodified_new.append('...')
            index_2[0] = r2

        if l2 != len(self.lines_1) + 1:
            for ii in range(l2, len(self.lines_1)):
                output_unmodified_original.append(self.lines_1[ii].strip('\n'))
        if r2 != (len(self.lines_2) + 1):
            for ii in range(r2, len(self.lines_2)):
                output_unmodified_new.append(self.lines_2[ii].strip('\n'))

        self.output_unmodified_original = output_unmodified_original
        self.output = output
        self.output_unmodified_new = output_unmodified_new

    def output_diff(self, diff):
        if self.output == ['chw']:
            self._get_answer_arrays(diff)
        for _ in self.output:
            print(_)

    def output_unmodified_from_original(self, diff):
        if self.output_unmodified_original == ['chw']:
            self._get_answer_arrays(diff)
        for _ in self.output_unmodified_original:
            print(_)

    def output_unmodified_from_new(self, diff):
        if self.output_unmodified_new == ['chw']:
            self._get_answer_arrays(diff)
        for _ in self.output_unmodified_new:
            print(_)

    def get_all_diff_commands(self):
        l = []
        N_1 = len(self.lines_1) + 1
        N_2 = len(self.lines_2) + 1
        table = [[0 for j in range(N_2)] for i in range(N_1)]
        for i in range(1, N_1):
            for j in range(1, N_2):
                if self.lines_1[i - 1].strip('\n') == self.lines_2[j - 1].strip('\n'):
                    l.append((i - 1, j - 1))
                    table[i][j] = table[i - 1][j - 1] + 1
                else:
                    table[i][j] = max(table[i - 1][j], table[i][j - 1])
        # if (N_1 - 1, N_2 - 1) not in l:
        l.append((N_1 - 1, N_2 - 1))
        answer = self._get_answer(l, table[N_1 - 1][N_2 - 1] + 1)
        return answer

    def get_lcs(self):
        table = [[0 for j in range(len(self.lines_2) + 1)] for i in range(len(self.lines_1) + 1)]
        for i in range(1, len(self.lines_1) + 1):
            for j in range(1, len(self.lines_2) + 1):
                if self.lines_1[i - 1].strip('\n') == self.lines_2[j - 1].strip('\n'):
                    table[i][j] = table[i - 1][j - 1] + 1
                else:
                    table[i][j] = max(table[i - 1][j], table[i][j - 1])


    def _get_answer(self, l, len_lcs):
        answer = []
        cc = list(combinations(l, len_lcs))
        answer_list = []
        for c in cc:
            for i, j in zip(c, c[1:]):
                if i[0] >= j[0] or i[1] >= j[1]:
                    break
            else:
                answer_list.append(c)
        for i in answer_list:
            last_point = (-1, -1)
            s = ''
            for ii in i:
                # print('last_point: ',last_point)
                if ii[0] - last_point[0] != 1 and ii[1] - last_point[1] != 1:
                    p1 = last_point[0] + 2
                    p2 = ii[0]
                    p3 = last_point[1] + 2
                    p4 = ii[1]
                    str = ''
                    if p1 == p2:
                        str += f'{p1}'
                    else:
                        str += f'{p1},{p2}'
                    str += 'c'
                    if p3 == p4:
                        str += f'{p3}'
                    else:
                        str += f'{p3},{p4}'
                    str += '\n'
                    s += str
                if ii[0] - last_point[0] == 1 and ii[1] - last_point[1] != 1:
                    p1 = last_point[1] + 2
                    p2 = ii[1]
                    if p1 != p2:
                        str = f'{last_point[0] + 1}a{p1},{p2}'
                    else:
                        str = f'{last_point[0] + 1}a{p1}'
                    str += '\n'
                    s += str
                if ii[0] - last_point[0] != 1 and ii[1] - last_point[1] == 1:
                    p1 = last_point[0] + 2
                    p2 = ii[0]
                    if p1 == p2:
                        str = f'{p1}d{ii[1]}'
                    else:
                        str = f'{p1},{p2}d{ii[1]}'
                    str += '\n'
                    s += str
                last_point = ii
            answer.append(s[:-1])
        return sorted(answer)


diff_1 = DiffCommands('diff_2.txt')
pair_of_files = OriginalNewFiles('file_3_1.txt', 'file_3_2.txt')
diff = pair_of_files.get_all_diff_commands()
print(diff[0])
# print(diff[0])
# pair_of_files.output_diff(diff_1)
# pair_of_files.output_unmodified_from_original(diff_1)
# pair_of_files.output_unmodified_from_new(diff_1)
# print(l)

# for i in s:
#     print(i)
