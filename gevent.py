import sys
import gevent
from random import randint

def job():
    """a job that sleeps for a random time between 1 to 10 seconds,
       returning the time in ms that it sleeps for."""
    min_time_in_ms = 1*1000
    max_time_in_ms = 10*1000
    sleep = randint(min_time_in_ms, max_time_in_ms)
    gevent.sleep(sleep/1000.0)
    return sleep

def main():
    """starts three threads in parallel.
       returns the result of the job in the list."""
    thread1 = gevent.spawn(job)
    thread2 = gevent.spawn(job)
    thread3 = gevent.spawn(job)
    gevent.joinall([thread1, thread2, thread3])
    return [thread1.value, thread2.value, thread3.value]

if __name__ == "__main__":
    print main()

