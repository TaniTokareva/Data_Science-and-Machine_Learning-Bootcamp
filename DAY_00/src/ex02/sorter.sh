#!/bin/bash

INPUT_FILE="../ex01/hh.csv"
OUTPUT_FILE="hh_sorted.csv"

{ head -n 1; sort -t',' -k 2 -k 1; } < "$INPUT_FILE" > "$OUTPUT_FILE"

