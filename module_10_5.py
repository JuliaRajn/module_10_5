import time
from multiprocessing import Pool
import os

def read_info(name):
    """
    Считывает информацию из файла построчно и добавляет ее в список.

    Args:
        name (str): Имя файла.

    Returns:
        None
    """
    all_data = []
    with open(name, 'r') as file:
        line = file.readline()
        while line:
            all_data.append(line)
            line = file.readline()


if __name__ == '__main__':
    # Список названий файлов (при условии, что файлы находятся в той же директории, что и скрипт)
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # Линейный вызов (закомментировать при запуске многопроцессного)
#start_time = time.time()
#for filename in filenames:
    #read_info(filename)
#end_time = time.time()
#print(f'Время выполнения (линейный): {time.strftime("%H:%M:%S", time.gmtime(end_time - start_time))}')

     #Многопроцессный вызов (закомментировать при запуске линейного)
    start_time = time.time()
    with Pool(processes=4) as pool:  # Используем 4 процесса
        pool.map(read_info, filenames)
    end_time = time.time()
    print(f'Время выполнения (многопроцессный): {time.strftime("%H:%M:%S", time.gmtime(end_time - start_time))}')
