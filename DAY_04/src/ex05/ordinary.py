#!/usr/bin/env python3

import sys
import psutil
import os

def read_file_lines(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.readlines()

def measure():

    process = psutil.Process()
    start_time = os.times()

    lines = read_file_lines(sys.argv[1])
    for _ in lines:
        pass

    end_time = os.times()
    peak_memory = process.memory_info().rss / (1024 ** 3)  # Конечная память в ГБ

    total_time = (end_time.user - start_time.user) + (end_time.system - start_time.system)
    return peak_memory, total_time

def main():
    peak_memory, total_time = measure()
    print(f"Peak Memory Usage = {peak_memory:.3f} GB")
    print(f"User Mode Time + System Mode Time = {total_time:.2f}s")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./ordinary.py <file_path>")
        sys.exit(1)
    main()
