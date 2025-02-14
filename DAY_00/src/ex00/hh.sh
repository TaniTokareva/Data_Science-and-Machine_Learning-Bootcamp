#!/bin/sh

OUTPUT_FILE=./hh.json
BASIC_URL=https://api.hh.ru
NUMBER_VACANCY=20

if [ $# -eq 1 ]; then
    curl -G -s "$BASIC_URL/vacancies?text=$1&per_page=$NUMBER_VACANCY" \
         | jq > $OUTPUT_FILE
else
    echo "Скрипту нужно передать название вакансии в качестве аргумента"
fi
