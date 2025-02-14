#!/bin/sh

OUTPUT_FILE="hh_positions.csv"

head -n 1 "$(ls *.csv | head -n 1)" > "$OUTPUT_FILE"

for file in *.csv; do
    if [ "$file" != "$OUTPUT_FILE" ]; then
        tail -n +2 "$file" >> "$OUTPUT_FILE"
    fi
done
