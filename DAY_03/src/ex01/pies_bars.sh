#!/bin/bash

# Установка необходимых библиотек
pip install termgraph
pip install colorama

# Запуск команды termgraph с вашим файлом данных и цветами
termgraph data.csv --color {blue,red}
