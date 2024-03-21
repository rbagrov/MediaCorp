


def task1():
    return 1

def task2():
    return 'pesho'


class MyException(Exception):
    
    pass


def run_tasks(tasks: list, orders: list):
    """
        tasks: [task1, task2, ...]; 
        order: [1, 2, 1, 3, 2, ...]
    """
    outputs = []
    
    if len(orders) == 0:
        raise MyException
    
    if  min(orders) < len(tasks) > max(orders):
        raise MyException

    for o in orders:
        try:
            task = tasks[o - 1]
            outputs.append(task())
        except IndexError:
            pass
    
    return outputs


outputs = run_tasks([task1, task2], [1, 2, 1])
print(outputs)