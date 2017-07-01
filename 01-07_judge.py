class multifilter:
    def judge_half(pos, neg):
	    return pos >= neg

    def judge_any(pos, neg):
		return pos >= 1

    def judge_all(pos, neg):
		return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
	    self.iterable = iterable
	    self.judge
        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция

    def __iter__(self):
	    for i in iterable:
		    yield i
        # возвращает итератор по результирующей последовательности