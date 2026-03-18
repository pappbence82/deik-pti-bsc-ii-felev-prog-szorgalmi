
import multiprocessing
import math

def burn_cpu():
    x = 0.0001
    while True:
        x = math.sqrt(x * x + 1.2345)

if __name__ == "__main__":
    multiprocessing.freeze_support()
    cores = multiprocessing.cpu_count()

    processes = []
    for _ in range(cores):
        p = multiprocessing.Process(target=burn_cpu)
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
