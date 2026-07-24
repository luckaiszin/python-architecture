import time

class Timer:

    def __init__(self):
        self.t_inicial = 0
    def __enter__(self):
        self.t_inicial = time.perf_counter()
        print('enter')
        return self

    def __exit__(self,exc_type, exc_val, exc_tb):
        t_final = time.perf_counter() - self.t_inicial
        print('bye bye: ',t_final)