# Параметры
num_of_steps = 3  
# Шаблон отчета
report_template = """Report

We have made {all_count} observations from tossing a coin: {tail_count} of them were tails and {head_count} of them were heads.
The probabilities are {tail_fract:.2f}% and {head_fract:.2f}%, respectively.
Our forecast is that in the next {num_of_steps} observations we will have: {forecast_tails} tail and {forecast_heads} heads.
"""

log_file ='analytics.log'


telegram_api_url = ""
bot =""
telegram_chat_id = ""
