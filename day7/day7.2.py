import time


def main():
    # print('Test:', solve(get_input('example1.txt')), '\n')
    print('Solution:', solve(get_input()))
    pass


def get_input(filepath='input.txt'):
    out = []
    with open(filepath, 'r') as f:
        raw = f.readlines()

    for line in raw:
        line = line.strip('\n').split(' ')
        out.append([line[7], line[1], ord(line[1]) - 4])
    return out


def solve(puzzle_input):
    workers = [None] * 5
    # Task = [ID, Dependants, work]
    tasks = {}
    elapsed = 0

    for entry in puzzle_input:
        if entry[0] in tasks.keys():
            tasks[entry[0]][0].append(entry[1])
        else:
            tasks[entry[0]] = [[entry[1]], entry[2]]

    for i in range(65, 91):
        if chr(i) not in tasks.keys():
            tasks[chr(i)] = [[], i - 4]

    while len(tasks) > 0:
        print(tasks)
        ready_queue = []
        for task in tasks.keys():
            if len(tasks[task][0]) == 0:
                ready_queue.append(task)

        while worker_free(workers) and len(ready_queue) > 0:
            workers = assign_task(workers, ready_queue[0], tasks)
            del ready_queue[0]


        result = run_work(workers)
        elapsed += result[1]
        for worker in result[0]:
            if worker[1] == 0:
                for task in tasks:


    return elapsed




def run_work(workers):
    elapsed = 0
    task_finished = False
    while not task_finished:
        for worker in workers:
            if worker is not None:
                worker[1] -= 1
                if worker[1] == 0:
                    task_finished = True
        elapsed += 1
    return workers, elapsed


def worker_free(workers):
    for worker_task in workers:
        if worker_task == None:
            return True
    return False


def assign_task(workers, task, tasks):
    i = 0
    while i < len(workers):
        if workers[i] == None:
            workers[i] = [task, tasks[task][1]]
            return workers
        i += 1


def elapse_time(workers, time):
    for i in range(len(workers)):
        workers[i][2] -= time
        if workers[i][2] < 0:
            raise Exception('Elapsed too much time, worker was allowed to idle.')
    return workers


def get_soonest_finsihed(workers):
    soonest = workers[0]
    for task in workers[1:]:
        if task[2] < soonest[2]:
            soonest = [task]
        elif task[2] == soonest[2]:
            soonest.append(task)
    soonest.sort()
    return soonest[0]


start_time = time.time()
main()
end_time = time.time()
print('\n' + ''.join(['-'] * 26) + '\nFINISHED\nTIME:', end_time - start_time,
      '\n' + ''.join(['-'] * 26))
input()
