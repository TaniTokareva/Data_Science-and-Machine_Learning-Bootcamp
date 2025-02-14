# Параметры
num_of_steps = 3  # Количество шагов для прогноза

# Шаблон отчета
report_template = """Report

We have made {all_count} observations from tossing a coin: {tail_count} of them were tails and {head_count} of them were heads.
The probabilities are {tail_fract:.2f}% and {head_fract:.2f}%, respectively.
Our forecast is that in the next {num_of_steps} observations we will have: {forecast_tails} tail and {forecast_heads} heads.
"""


report = """Report
We have made {total} observations from tossing a coin: {reshkas} of them were tails and {orels} of them were heads. 
The probabilities are {reshkas_percent:.2f}% and {orels_percent:.2f}%, respectively. 
Our forecast is that in the next {steps} observations we will have: {forecast_reshkas} tail(s) and {forecast_orels} head(s)."""
