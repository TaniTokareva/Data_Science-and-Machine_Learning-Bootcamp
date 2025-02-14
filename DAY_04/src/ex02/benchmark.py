#!/usr/bin/env python3

import timeit
import sys

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

def filter_emails_filter(emails):
    return(list(filter(lambda email: 'gmail.com' in email, emails)))


def benchmark(method, reps):
    if method == 'loop':
        time = timeit.timeit(lambda: filter_emails_loop(emails), number=reps)
    elif method == "comprehension":
        time = timeit.timeit(lambda: filter_emails_comprehension(emails), number=reps)
    elif method == 'map':
        time = timeit.timeit(lambda: filter_emails_map(emails), number=reps)
    elif method == 'filter':
        time = timeit.timeit(lambda: filter_emails_filter(emails), number=reps)
    else: 
        raise Exception ("Incorrect method")
    return time


if __name__ == "__main__":

    if len(sys.argv) == 3:
        method = sys.argv[1]
        try:
            reps = int(sys.argv[2])
        except ValueError:
            print("Error: reps must be an integer")    
            sys.exit(1)
        try:
            time = benchmark(method, reps)
            print(time)
        except ValueError as e:
            print(e)
            sys.exit(1)
    else:
        print("Error: Incorrect number of args")
        sys.exit(1)