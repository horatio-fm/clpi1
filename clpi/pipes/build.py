from collections import deque

from clpi.settings.base import *
from clpi.tasks.first import *


def build_pipe(pipe):
    fifo = deque(pipe)
    assemble = []
    while len(fifo) > 0:

        ele = fifo.popleft()
        if ele.startswith("END"):
            break
        if ele == "":
            continue
        if not ele[0].isalpha():
            continue

        task_name = ele
        inp, out = [], []
        ele = fifo.popleft()
        while not ele.startswith("___"):
            if ele == "":
                ele = fifo.popleft()
                continue
            if ele[0] == ">":
                inp.append(Pstr(ele.split()[-1]))
            if ele[0] == "<":
                out.append(ele.split()[-1])
            ele = fifo.popleft()

        task = globals()[task_name + "Task"]
        instance_task = task(inp, out, gl_vars)
        assemble.append(instance_task)

    return assemble
