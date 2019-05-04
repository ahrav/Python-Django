## Processes is a 2D array, each item has dependencies in same list.

def build_order(processes):
    temp_mark = set()
    perm_mark = set()
    result = []
    for i in range(len(processes)):
        if i not in perm_mark:
            visit(i, processes, temp_mark, perm_mark, result)

    return result

def visit(process, processes, temp_mark, perm_mark, result):
    if process in temp_mark:
        return "error"
    if process not in perm_mark:
        temp_mark.add(process)
        for i in processes[process]:
            visit(i, processes, temp_mark, perm_mark, result)
        perm_mark.add(process)
        temp_mark.remove(process)
        result.append(process)


def build_order2(processes):
    temp_mark = set()
    perm_mark = set()
    result = []
    for i in range(len(processes)):
        if i not in perm_mark:
            visit(i, proceses, temp_mark, perm_mark, result)

    return result

def visit(i, process, temp_mark, perm_mark, result):
    if process in temp_mark:
        return 'error'
    if process not in perm_mark:
        temp_mark.add(process)
        for i in processes[process]:
            visit(i, processes, temp_mark, perm_mark, result)
        perm_mark.add(process)
        temp_mark.remove(process)
        result.append(process)