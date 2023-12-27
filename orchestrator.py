import subprocess
import time

def run_mapper(matrix_a, matrix_b):
    proceso_mapper = subprocess.Popen(['python', 'mapper.py',matrix_a,matrix_b], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    return proceso_mapper


def run_sort(input_stream):
    proceso_sort = subprocess.Popen(['sort'], stdin=input_stream, stdout=subprocess.PIPE)
    input_stream.close()
    return proceso_sort



def run_reducer(input_stream):
    proceso_reducer = subprocess.Popen(['python', 'reducer.py'], stdin=input_stream)
    input_stream.close()
    return proceso_reducer

def wait_for_processes(*processes):
    for proceso in processes:
        proceso.wait()


def main():
    matrix_a = 'matrixD.txt'
    matrix_b = 'matrixD.txt'

    proceso_mapper = run_mapper(matrix_a, matrix_b)
    proceso_sort = run_sort(proceso_mapper.stdout)
    proceso_reducer = run_reducer(proceso_sort.stdout)

    wait_for_processes(proceso_mapper, proceso_sort, proceso_reducer)
    

if __name__ == "__main__":
    start_time = time.time()

    main()

    print("--- %s seconds ---" % (time.time() - start_time))