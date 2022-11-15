# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION


# Assignments to a CircularList object will only involve integer indexes.
#
# When the index is an integer, it is interpreted modulo the length
# of the list.
#
# When working with slices:
# - The last argument of a slice cannot be equal to 0.
# - When the last argument of a slice is not given, it is set to 1.
# - When the first argument of a slice is not given, it is set to
#   0 or to -1 depending on the sign of the last argument.
# - When the second argument of a slice is not given, it is set to
#   len(list) or to -len(list) -1 depending on the sign of the last argument.
# - Denoting by L the CircularList object, returns a list consisting of
#   all elements of the form L[i modulo len(L)] for i ranging between first
#   (included) and second (excluded) arguments of slice, in steps given by
#   third argument of slice.

class CircularList:
    def __init__(self, *L):
        self.L = list(L)

    def __str__(self):
        return str(self.L)
    # REPLACE PASS ABOVE WITH YOUR CODE

    def __len__(self):
        return len(self.L)

    def __getitem__(self, item):
        if type(item) is int:
            item = item % len(self.L)
            return self.L[item]
        if type(item) is slice:
            if item.step == 0:
                raise ValueError('slice step cannot be zero')
            start, stop, step = item.start, item.stop, item.step
            if step is None:
                step = 1
            if start is None:
                if step < 0:
                    start = -1
                else:
                    start = 0
            if stop is None:
                if step < 0:
                    stop = -len(self.L) - 1
                else:
                    stop = len(self.L)
            length = len(self.L)
            count = abs(start // length) + abs(stop // length) + 1 # right side
            new_l = self.L * count
            if step > 0:
                if stop < start:
                    start, stop = 1, 0
                else:
                    if start < 0:
                        offset = abs(start // length) * length
                        start += offset
                        stop += offset
            else:
                if stop > start:
                    start, stop = 0, 1
                else:
                    if stop < 0:
                        offset = abs(stop // length) * length
                        start += offset
                        stop += offset
            return new_l[start:stop:step]


    def __setitem__(self, key, value):
        key = key % len(self.L)
        self.L[key] = value

L = CircularList(*range(10, 20))
print(L[-10:-20:-1])