from main import run_tasks

def task1():
    return 1

def task2():
    return 'pesho'


def test():
    tasks = [task1, task2]
    order = [1, 2, 1]

    output = run_tasks(tasks, order)
    if output == [1, 'pesho', 1]:
        return True
    else:
        return False
    

if test():
    print('success')