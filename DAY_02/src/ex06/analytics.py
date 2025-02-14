import logging
import requests
from random import randint
from config import log_file, telegram_api_url, telegram_chat_id, bot

logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format='%(asctime)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)

class Research():
    def __init__(self, path):
        self.path = path
        logging.info(f"Initialized Research with path: {self.path}")
        
    def file_reader(self, has_header=True):
        logging.info("Starting to read the file")        
        with open(self.path, 'r') as file:
            text = file.read()          
        
        lines = text.split('\n')
        
        if len(lines) < 2:
            logging.error("Incorrect number of lines")
            raise Exception("Incorrect number of lines")
            
        header = lines[0].strip().split(',')

        if len(header) != 2 or header != ['head', 'tail']:
            logging.error("Incorrect header of table")
            raise Exception("Incorrect header of table")
        
        if has_header:
            index = 1  # Начнем с 1, если есть заголовок
        else:
            index = 0  # Если нет заголовка, начнем с 0
        data = []  # Место для хранения данных
        for line in lines[index:]:
            line = line.strip()
            if line:  # Проверим, не пуста ли строка
                values = line.split(',')
                if len(values) != 2 or values[0] not in ['0', '1'] or values[1] not in ['0', '1']:
                    logging.error("Incorrect data")
                    raise Exception("Incorrect data")
                data.append([int(val) for val in values])  # Добавляем строку в данные
        logging.info(f"File read successfully with {len(data)} rows")
        return data


    class Calculations():
        
        def __init__(self, data):
            logging.info(f"Initialized Calculations")
            self.data = data # Данные передаются в конструктор
            

        def counts(self, data):
            logging.info("Calculating the counts of heads and tails")
            head_count = 0
            tail_count = 0 
            for row in data:
                if row[0] == 1:
                    head_count += 1
                if row[1] == 1:
                    tail_count += 1
            logging.info(f"Head count: {head_count}, Tail count: {tail_count}")
            return head_count, tail_count
        
        def fractions(self, head_count, tail_count):
                all_count = head_count + tail_count
                if all_count == 0:
                    logging.warning("total count = 0, fractions = 0")
                    return 0,0
                head_fract = (head_count / all_count) * 100
                tail_fract = (tail_count / all_count) * 100
                logging.info(f"Head fractions: {head_fract}%, Tail fractions: {tail_fract}% ")
                return head_fract, tail_fract
    
    class Analytics(Calculations):
        def __init__(self, data):
            super().__init__(data)  # Инициализация родительского класса
            logging.info("Initialized Analytics")

        def predict_random(self, num_of_steps) :
            predictions = []
            logging.info(f"Predicting for {num_of_steps}")
            for _ in range (num_of_steps):
                x = randint(0,1)
                prediction = [x, 1 - x]
                predictions.append(prediction)
            logging.info(f"Predictions: {predictions}")
            return predictions

        def predict_last(self):
            logging.info("Getting the last element of data")
            return self.data[-1] if self.data else []
        
        def save_file(self, data, file_name, extension='txt'):
            with open(f'{file_name}.{extension}', 'w') as file: #????
                logging.info(f"File {file_name} saved")
                file.write(data)
                
        def send_telegram_message(self, success=True):
            message = "The report has been successfully created" if success == True else "The report hasn’t been created due to an error"
            logging.info(f"Sending Telegram message: {message}")
            payload = {
                "chat_id": telegram_chat_id,
                "text": message
            }
            try:
                response = requests.post(telegram_api_url.format(bot=bot), data=payload)
                if response.status_code == 200:
                    logging.info("Telegram message sent successfully")
                else:
                    logging.error(f"Failed to send Telegram message: {response.status_code}, Response: {response.text}")
            except Exception as e:
                logging.error(f"Error while sending Telegram message: {e}")
        