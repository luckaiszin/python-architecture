import time
from contextlib import contextmanager

@contextmanager
def Timer():
    # --- CÓDIGO DE ENTRADA (Equivalente ao __enter__) ---
    t_inicial = time.perf_counter()
    
    try:
        # O yield passa o controle para dentro do bloco 'with'
        # Se você quisesse usar "as t", poderia fazer "yield t_inicial"
        yield 
        
    finally:
        # --- CÓDIGO DE SAÍDA (Equivalente ao __exit__) ---
        # O bloco finally garante que o tempo será medido mesmo se der erro no meio do código
        tempo_gasto = time.perf_counter() - t_inicial
        print(f'Tempo: {tempo_gasto:.3f}s')

# Testando o novo Context Manager
with Timer():
    print('Executando alguma tarefa pesada...')
    time.sleep(2)