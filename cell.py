def intersection(a, b):
    return a[0] & b[0], a[1] & b[1]


def combine(a, b):
    K = 0
    c = {(0, 0): 0}
    for k1, v1 in a.items():
        for k2, v2 in b.items():
            k = intersection(k1, k2)
            if k == (0, 0):
                K += v1 * v2
            else:
                if k in c:
                    c[k] += v1 * v2
                else:
                    c[k] = v1 * v2
    t = 1 / (1 - K)
    for i in c:
        c[i] *= t
    return c


class DSCell:
    def __init__(self, p: float = 0.5):
        self.p = DSCell.__get_ds(p)

    def update(self, value: float):
        self.p = combine(self.p, DSCell.__get_ds(value))

    @staticmethod
    def __get_ds(p: float):
        return {
            (0, 0): 0,
            (1, 0): 1 - p - 0.05,
            (0, 1): p - 0.05,
            (1, 1): 0.1
        }

    def get_p(self):
        return self.p[(0, 1)] + self.p[(1, 1)] / 2

    def get_score(self) -> float:
        return self.get_p()


class Cell:
    def __init__(self, p: float = 0.5):
        self.sum = p
        self.n = 1

    def update(self, value: float):
        self.sum += value
        self.n += 1

    def get_p(self):
        return self.sum / self.n

    def get_score(self) -> float:
        return self.get_p()
