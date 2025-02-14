#/bin/sh

INPUT_FILE="../ex03/hh_position.csv"
OUTPUT_FILE="hh_uniq_position.csv"

echo name,count > $OUTPUT_FILE

tail -n +2 $INPUT_FILE | awk -F ',' '{print $3}' | sort | uniq -c | while read count name; do
  echo $name,$count >> $OUTPUT_FILE
  done