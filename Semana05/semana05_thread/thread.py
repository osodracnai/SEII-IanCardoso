import concurrent.futures
import time
import threading

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleepin {seconds} seconds')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

#
with concurrent.futures.ThreadPoolExecutor() as executor:

    f1 = executor.submit(do_something,1)   #agenda uma função a ser executada e retorno um objeto futuro
    secs = [5, 4, 3, 2, 1]
    results = [executor.submit(do_something, secs) for sec in secs] #envia a função do_something com argumento de cada segundo na lista secs
    for f in concurrent.futures.as_completed(results): #roda as funções na lista results conforme são terminadas
       print(f.result())

    results = executor.map(do_something, secs)   #mapeia as funções na lista results conforme são iniciadas
    for result in results:
       print(result)
"""threads = []

for _ in range(10):

    t = threading.Thread(target=do_something, args=[1.5]) #Seta a função do_something como o alvo da thread
    t.start()           #inicia a thread
    threads.append(t)   #coloca ultima thread no fim do array threads[]

for t in threads:
    t.join()            #junta todos elementos de threads[]
"""
finish=time.perf_counter()