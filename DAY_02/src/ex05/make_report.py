import sys
from analytics import Research
from config import num_of_steps, report_template

def main():
    #1. Получение данных из файла
    data = Research(sys.argv[1]).file_reader()

    calc = Research.Calculations(data)
    analytics = Research.Analytics(data)
    #2.
    head_count, tail_count = calc.counts(data)
    head_fract, tail_fract = calc.fractions(head_count, tail_count)
    #3.
    predictions = analytics.predict_random(num_of_steps)
    last_prediction = analytics.predict_last()
    #4.
    forecast_tails = sum([pred[1] for pred in predictions])
    forecast_heads = num_of_steps - forecast_tails

    #5. Генерация текста репорта
    report = report_template.format(
        all_count = head_count + tail_count,
        tail_count=tail_count,
        head_count=head_count,
        tail_fract=tail_fract,
        head_fract=head_fract,
        num_of_steps=num_of_steps,
        forecast_tails=forecast_tails,
        forecast_heads=forecast_heads

    )

    # Сохраняем отчет в файл
    analytics.save_file(report, 'forecast_report', 'txt')
    print(report)

if __name__ == "__main__":
    main()