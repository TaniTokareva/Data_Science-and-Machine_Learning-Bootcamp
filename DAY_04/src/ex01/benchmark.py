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

def filter_emails_map(emails):
    return list(map(lambda email: email if 'gmail.com' in email else None, emails))

def benchmark():
    reps = 900000
    loop_time = timeit.timeit(lambda: filter_emails_loop(emails), number=reps)
    comprehension_time = timeit.timeit(lambda: filter_emails_comprehension(emails), number=reps)
    map_time = timeit.timeit(lambda: filter_emails_map(emails), number=reps)
    if (comprehension_time < loop_time and comprehension_time < map_time):
        print("it is better to use a list comprehension")
    elif (loop_time < comprehension_time and loop_time < map_time):
        print("it is better to use a loop")
    elif (map_time < loop_time and map_time < comprehension_time):
        print("it is better to use a map")
    
    times = sorted([loop_time, comprehension_time, map_time])
    print(f"{times[0]} vs {times[1]} vs {times[2]}")


if __name__ == "__main__":
    benchmark()