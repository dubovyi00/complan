from random import randint

def rand_str():
	return "".join(chr([randint(48, 57), randint(65, 90), randint(97, 122)][randint(0, 2)]) for _ in range(10))

