import time


def timefun(fn):
    def wrapper(*args, **kwargs):
        st = time.time()
        res = fn(*args, **kwargs)
        dt = time.time() - st
        print(f"Время работы: {dt} сек")
        return res
    return wrapper


@timefun
def linear_search(sequence, look_for):
    i = 0
    length = len(sequence)
    while i < length and look_for != sequence[i]:
        i += 1
    return i if i < length else None


linear_search([100000, 5, 4, 3, 6, 88, 99], 99)


@timefun
def linear_search_virt(sequence, look_for):
    i = 0
    sequence.append(look_for)
    length = len(sequence) - 1
    while look_for != sequence[i]:
        i += 1
    return i if i < length else None


linear_search_virt([100000, 5, 4, 3, 6, 88, 99], 99)
