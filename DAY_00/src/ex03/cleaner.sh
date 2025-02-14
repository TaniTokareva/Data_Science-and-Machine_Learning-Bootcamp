#!/bin/sh

INPUT_FILE=../ex02/hh_sorted.csv
OUTPUT_FILE=hh_position.csv

head -n 1 $INPUT_FILE > $OUTPUT_FILE

tail -n +2 $INPUT_FILE | while IFS=',' read -r id created_at name has_test alternate_url; do

  if echo $name | grep -q -i "Junior"; then
    grade="\"Junior\""
  elif echo $name | grep -q -i "Middle"; then
    grade="\"Middle\""
  elif echo $name | grep -q -i "Senior"; then
    grade="\"Senior\""
  else
    grade="\"-\"";
  fi


  echo $id,$created_at,$grade,$has_test,$alternate_url >> $OUTPUT_FILE

done
