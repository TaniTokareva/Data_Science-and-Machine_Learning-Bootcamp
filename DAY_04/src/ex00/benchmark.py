#!/usr/bin/env python3
import timeit

emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 
'anna@live.com', 'philipp@gmail.com'] * 5

def filter_emails_loop(emails):
    result = []
    for email in emails:
        if ('gmail.com' in email):
            result.append(email)
    return result

def filter_emails_comprehension(emails):
    return[email for email in emails if 'gmail.com' in email]

def benchmark():
    reps = 90000
    loop_time = timeit.timeit(lambda: filter_emails_loop(emails), number=reps)
    comprehension_time = timeit.timeit(lambda: filter_emails_comprehension(emails), number=reps)
    if (comprehension_time < loop_time):
        print("it is better to use a list comprehension")
    elif (loop_time < comprehension_time):
        print("it is better to use a loop")
    
    times = sorted([loop_time, comprehension_time])
    print(f"{times[0]} vs {times[1]}")


if __name__ == "__main__":
    benchmark()