import time



def random_number_generator(seed = None, a = 1103515245, c = 12345, m = 2 ** 31):
    if seed is None:
        seed = int(time.time() * 1000) % m
    while True:
        seed = (a * seed + c) % m
        yield seed % 101
