from collections import defaultdict
from re import findall

from levenshtein_distance import *


# Words in the text are defined as being ALL LOWERCASE,
# NOT preceded and NOT followed by a letter (be it lowercase or uppercase),
# and OF LENGTH STRICTLY GREATER THAN 3.
#
# A word in the text is not in the dictionary if its all uppercase version
# is not in the dictionary.
#
# Words in the text that are not in the dictionary AND THAT OCCUR
# AT LEAST TWICE IN THE TEXT are output, followed by the line number(s)
# where they occur in the text (line numbers are output only once in the
# unlikely case such words would appear more than once on the same line),
# two successive line numbers being separated by a comma and a space.
# Lines in the text are numbered starting from 1.
# You might find the enumerate() function useful.
#
# You will score marks if you do not also output associated suggestion(s),
# namely, the (lowercase version) of the word(s) in the dictionary whose
# Levenshtein distance to the unknown word is minimal.
# For the program to be efficient enough, it is necessary to slightly edit
# (in a straightforward way) levenshtein_distance.py.
# You should then get the output within 30 seconds.
#
# Both dictionary.txt and the file whose name is provided as argument to
# the function are stored in the working directory.
#
# Will be tested on other text files, of a similar size as the sample file.
# Written by Eric Martin for COMP9021


'''
Given 2 words, creates an object which can provide the Levenshtein
distance between both words, the alignments of minimal cost between both
words, and the display of those alignments. The costs for insertion,
deletion and substitution are set by default to 1, 1 and 2,
respectively, but can be changed.
'''


class Levenshtein_distance:
    '''
    Given two words word_1 and word_2, builds a table of distances and
    backtraces for the initial segments of word_1 and word_2, from which
    the Levenshtein distance between both words can be computed, as well
    as the possible alignments of minimal distance between both words.
    '''

    def __init__(self, word_1, word_2, insertion_cost=1, deletion_cost=1,
                 substitution_cost=2
                 ):
        self.word_1 = word_1
        self.word_2 = word_2
        self.insertion_cost = insertion_cost
        self.deletion_cost = deletion_cost
        self.substitution_cost = substitution_cost
        self._table = self._get_distances_and_backtraces_table()

    def _get_distances_and_backtraces_table(self):
        N_1 = len(self.word_1) + 1
        N_2 = len(self.word_2) + 1
        # Think of table as a sequence of columns, read from left to
        # right, each column being read from bottom to top, with word_1
        # and word_2 positioned as follows.
        #
        #  2
        #  _
        #  d
        #  r
        #  o
        #  w
        #  .
        #    . w o r d _ 1
        #
        # Each position in the sequence of columns will record the
        # minimal cost of converting the corresponding initial segment
        # of word_1 with the corresponding initial segment of word_2,
        # and also the last move -- horizontal, vertical, diagonal --
        # from a neighbouring position -- left, below, or left and
        # below, respectively -- that can yield this minimal cost.
        # '/' corresponds to a substitution.
        # '-' corresponds to a deletion.
        # '|' corresponds to an insertion.
        table = [[(0, []) for _ in range(N_2)] for _ in range(N_1)]
        # Bottom row: cost of deleting more and more letters from
        # word_1.
        for i in range(1, N_1):
            table[i][0] = i, ['-']
        # Leftmost column: cost of insertion more and more letters from
        # word_2.
        for j in range(1, N_2):
            table[0][j] = j, ['|']
        d = {}
        # Processing all other rows from bottom to top, and each row
        # from left to right, determine the cost of each possible
        # operation:
        # - deleting current letter (of index i-1) of word_1;
        # - inserting current letter (of index j-1) of word_2;
        # - matching or substituting currents letters of word_1 and
        #   word_2.
        for i in range(1, N_1):
            for j in range(1, N_2):
                d['-'] = table[i - 1][j][0] + self.deletion_cost
                d['|'] = table[i][j - 1][0] + self.insertion_cost
                d['/'] = table[i - 1][j - 1][0] \
                    if self.word_1[i - 1] == self.word_2[j - 1] \
                    else table[i - 1][j - 1][0] + self.substitution_cost
                minimal_cost = min(d.values())
                table[i][j] = minimal_cost, \
                              [x for x in d if d[x] == minimal_cost]
        return table

    # We start at the top right corner of _backtraces, where we find the
    # last directions taken to get there at minimal cost, and move
    # backwards all the way to the bottom left corner, eventually
    # generating all paths from the bottom left corner to the top right
    # corner that yield that minimal cost.
    def _compute_alignments(self, i, j):
        if i == j == 0:
            yield '', ''
        if '/' in self._backtraces[i][j]:
            for pair in self._compute_alignments(i - 1, j - 1):
                yield pair[0] + self.word_1[i - 1], \
                      pair[1] + self.word_2[j - 1]
        if '-' in self._backtraces[i][j]:
            for pair in self._compute_alignments(i - 1, j):
                yield pair[0] + self.word_1[i - 1], pair[1] + '_'
        if '|' in self._backtraces[i][j]:
            for pair in self._compute_alignments(i, j - 1):
                yield pair[0] + '_', pair[1] + self.word_2[j - 1]

    def distance(self):
        '''
        Returns the Levenshtein distance equal to the minimum number
        of deletions, insertions and substitutions needed to transform
        the first word into the second word, with deletions and
        insertions incurring a cost of 1, and substitutions incurring a
        cost of 2.

        >>> Levenshtein_distance('', '').distance()
        0

        >>> Levenshtein_distance('ABCDE', '').distance()
        5

        >>> Levenshtein_distance('', 'ABCDE').distance()
        5

        >>> Levenshtein_distance('A', 'A').distance()
        0

        >>> Levenshtein_distance('A', 'B').distance()
        2

        >>> Levenshtein_distance('AA', 'A').distance()
        1

        >>> Levenshtein_distance('PARIS', 'LONDON').distance()
        11

        >>> Levenshtein_distance('PAPER', 'POPE').distance()
        3

        >>> Levenshtein_distance('DEPART', 'LEOPARD').distance()
        5
        '''
        return self._table[len(self.word_1)][len(self.word_2)][0]

    def get_aligned_pairs(self):
        '''
        Returns the list of all possible ways to transform the first
        word into the second word and minimising the Levenshtein
        distance.

        >>> Levenshtein_distance('', '').get_aligned_pairs()
        [('', '')]

        >>> Levenshtein_distance('ABCDE', '').get_aligned_pairs()
        [('ABCDE', '_____')]

        >>> Levenshtein_distance('', 'ABCDE').get_aligned_pairs()
        [('_____', 'ABCDE')]

        >>> Levenshtein_distance('A', 'A').get_aligned_pairs()
        [('A', 'A')]

        >>> Levenshtein_distance('A', 'B').get_aligned_pairs()
        [('A', 'B'), ('_A', 'B_'), ('A_', '_B')]

        >>> Levenshtein_distance('AA', 'A').get_aligned_pairs()
        [('AA', '_A'), ('AA', 'A_')]

        >>> Levenshtein_distance('PAPER', 'POPE').get_aligned_pairs()
        [('PAPER', 'POPE_'), ('P_APER', 'PO_PE_'), ('PA_PER', 'P_OPE_')]

        >>> len(Levenshtein_distance('PARIS',\
                                     'LONDON'\
                                    ).get_aligned_pairs())
        3653
        '''
        return list(self._compute_alignments(len(self.word_1),
                                             len(self.word_2)
                                             )
                    )

    def display_all_aligned_pairs(self):
        '''
        Displays all possible ways to transform the first word
        into the second word and minimising the Levenshtein distance.

        >>> Levenshtein_distance('DEPART',\
                                 'LEOPARD'\
                                ).display_all_aligned_pairs()
        DE_PART
        LEOPARD
        <BLANKLINE>
        _DE_PART
        L_EOPARD
        <BLANKLINE>
        D_E_PART
        _LEOPARD
        <BLANKLINE>
        DE_PAR_T
        LEOPARD_
        <BLANKLINE>
        _DE_PAR_T
        L_EOPARD_
        <BLANKLINE>
        D_E_PAR_T
        _LEOPARD_
        <BLANKLINE>
        DE_PART_
        LEOPAR_D
        <BLANKLINE>
        _DE_PART_
        L_EOPAR_D
        <BLANKLINE>
        D_E_PART_
        _LEOPAR_D
        '''
        print('\n\n'.join('\n'.join((pair[0], pair[1]))
                          for pair in self.aligned_pairs
                          )
              )

def f(filename):
    # '''
    # >>> f('atale_poe.txt')
    # minarets: 193, 206
    #     Did you mean minaret?
    # oriels: 194, 206
    #     Did you mean oils or ores or orgies or tories?
    # vermicular: 368, 375
    #     Did you mean vehicular?
    # '''
    lines = open(filename, 'r').readlines()
    fin = open('dictionary.txt', 'rt')
    d = set([i.strip('\n') for i in fin.readlines()])
    dic = defaultdict(int)
    dic_list = defaultdict(list)
    l = []
    for i,line in enumerate(lines,1):
        for word in line.split():
            word = word.strip('.').strip(',').strip('\'')
            if len(word) <= 3 or word[0].isupper() or not word.isalpha():
                continue
            if word.upper() not in d:
                dic[word] += 1
                dic_list[word].append(i)
                if dic[word] >=2:
                    print(word, ': ',end='')
                    for number in dic_list[word]:
                        print(number,end='')
                        if number != dic_list[word][-1]:
                            print(', ',end='')
                    print()
                    print('    Did you mean ')
                    answerlist = findallpossible(word,d)
                    print(answerlist)
    # REPLACE PASS ABOVE WITH YOUR CODE
def findallpossible(word,d):
    s_dis = len(word)
    for i in d:
        dis = Levenshtein_distance(word, i).distance()
        if dis < s_dis:
            s_dis = dis
if __name__ == '__main__':
    import doctest
    doctest.testmod()