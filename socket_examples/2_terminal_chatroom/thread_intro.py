import threading


# Threading allows us to speed up programs by executing multiple tasks at the same time.
# Each task will run on its own thread
# Each thread can run simultaneously and share data with each other

# Every thread when you start it must do something, which we can define with a function.
# Our threads will the target these functions.
# When we start the threads, the target will be run.

def function1():
    for i in range(10):
        print('ONE ')


def function2():
    for i in range(10):
        print('TWO ')


def function3():
    for i in range(10):
        print('THREE ')

# If we call these functions, we see the first function call MUST complete before the next.
# They are executed linearly.
# function1()
# function2()
# function3()

# We can execute these functions concurrently using threads!
# We must have a target for a thread.
t1 = threading.Thread(target=function1)
t2 = threading.Thread(target=function2)
t3 = threading.Thread(target=function3)

t1.start()
t2.start()
t3.start()

# Threads can only be run once. If you want to reuse, you must redefine.
t1 = threading.Thread(target=function1)
t1.start()

# If you want to 'pause' the main program until a thread is done you can!
t1 = threading.Thread(target=function1)
t1.start()
# This pauses the main program until the thread is complete
t1.join()
print('Threading Rules!')