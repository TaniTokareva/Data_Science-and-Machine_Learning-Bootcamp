#!/bin/sh
INPUT_FILE="../ex00/hh.json"
OUTPUT_FILE="hh.csv"
FILTER_FILE="filter.jq"

jq -fr $FILTER_FILE $INPUT_FILE > hh.csv
