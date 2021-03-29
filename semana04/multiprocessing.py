#Ian Cardoso - 11411EMT014

#objetivo: executar código simultaneamente utilizando o multiprocessamento

import concurrent.futures
#importando a biblioteca de tempo
import time

#iniciando um contador para verificar quanto tempo o script leva para ser processado
start = time.perf_counter()

#função utilizada para imprimir 
def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
     #imprimindo quantos segundos se passaram
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'


with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)

#aqui termina o código que verifica o tempo
finish = time.perf_counter()

#imprimindo o tempo total que levou para processar o codigo
print(f'Finished in {round(finish-start, 2)} second(s)')
