import time

from multicore import initialize, shutdown, Task
from multicore.utils import ranges


# Note the scoping of the "items" variable and the functions
items = range(100)


def as_string(item):
    for i in range(item):
        print(f'{i},')


def expensive_as_string(item):
    time.sleep(0.01)
    return str(item)


def multi_expensive_as_string(start, end):
    return ",".join([expensive_as_string(item) for item in items[start:end]])


if __name__ == "__main__":

    # Needs to be called only once for lifetime of process
    initialize()

    # Example 1: trivial (and slightly pointless) usage
    task = Task()

    task.run(as_string, 2000)


    # Example 2: divide job optimally using ranges function
    #task = Task()
    #for start, end in ranges(items):
        # Note we don't pass items because pickling is expensive and defeats
        # the purpose of the exercize.
     #   task.run(multi_expensive_as_string, start, end)
   # print(", ".join(task.get()))

    # Stop the multicore workers
    shutdown()