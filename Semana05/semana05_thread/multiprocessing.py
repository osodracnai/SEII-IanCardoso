import concurrent.futures
import time
import multiprocessing


start = time.perf_counter()


def do_something(seconds):  #função que 'dorme' a quantidade de segundos passados como argumentos
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

p1 = multiprocessing.Process(target=do_something)  #cria um objeto multiprocessing e coloca a função do_something como alvo
p2 = multiprocessing.Process(target=do_something)

p1.start()  #inicia o processo e printa o fim do processo antes que ele acabe (dorme 1 segundo)
p2.start()

p1.join()  #garante que o processo acabe antes de seguir no script
p2.join()


'''No código abaixo foi criado uma lista de processos. A cada vez que passa pelo laço é criado um processo
com alvo em 'do_something', o processo é iniciado e colocado no fim da lista de processos. Apenas quando todos os processos
são criados e iniciados que será percorrido cada processo na lista processes e com o método join que garante o fim do processo
antes que o script siga para calcular o tempo total'''

processes = []
for _ in range(10):
    p = multiprocessing.Process(target=do_something)
    p.start()
    processes.append(p)

for process in processes:
    process.join()



'''
ProcessPoolExecutor é padrão do python e pode ser usado para criar e gerenciar processos
A linha 45 faz com que os processos sejam submetidos um de cada vez
A linha 46 (.map) roda a função conforme são executadas para cada segundo na lista secs
 na ordem que foram iniciados'''

with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    #results = [executor.submit(do_something, sec) for sec in secs]
    results = executor.map(do_something, secs)

    for result in results:
        print(result)

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')