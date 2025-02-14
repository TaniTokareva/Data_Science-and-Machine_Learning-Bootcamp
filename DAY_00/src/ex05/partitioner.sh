#!/bin/sh
rm -f *.csv

INPUT_FILE="../ex03/hh_position.csv"

tail -n +2 $INPUT_FILE | awk -F ',' '
{
    date=substr($2, 2, 10)
    if (!seen[date]) {
        output_file = date ".csv"
        # head -n 1 $INPUT_FILE > output_file
        print "\"id\",\"created_at\",\"name\",\"has_test\",\"alternate_url\"" > output_file
        seen[date] = 1
    }
    print $0 >> output_file
}
'
