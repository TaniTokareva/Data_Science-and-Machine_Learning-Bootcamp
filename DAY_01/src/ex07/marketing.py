import sys


# Первый список - это учетные записи электронной почты ваших клиентов. 
# Второй список содержит учетные записи электронной почты участников вашего последнего мероприятия
# (некоторые из них были вашими клиентами). Третий список содержит учетные записи ваших клиентов, которые
# просмотрели ваше последнее рекламное электронное письмо.


clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
           'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
           'elon@paypal.com', 'jessica@gmail.com']
participants = ['walter@heisenberg.com', 'vasily@mail.ru',
                'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
                'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']

#1.  Создайте список тех, кто еще не видел ваше рекламное электронное письмо. Список
#будет отправлен в колл-центр, чтобы связаться с этими людьми.
def call_center():
    clients_set = set(clients)
    recipients_set = set(recipients)
    result = list(clients_set - recipients_set)
    return result

#2. Создайте список участников, которые не являются вашими клиентами. 
# Вы отправите им электронное письмо с информацией о ваших продуктах.

def potential_clients():
    clients_set = set(clients)
    participants_set = set(participants)
    result = list(participants_set - clients_set)
    return result

#3. Создайте список клиентов, которые не участвовали в мероприятии. Вы отправите им
# ссылку на видео и слайды с мероприятия.

def loyalty_program():
    clients_set = set(clients)
    participants_set = set(recipients)
    result = list(clients_set - participants_set)
    return result

def marketing(command):
    if command == 'call_center':
        return call_center()
    elif command == 'potential_clients':
        return potential_clients()
    elif command == 'loyalty_program':
        return loyalty_program()
    else:
        raise Exception ("Incorrect command")

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        print(marketing(sys.argv[1]))
    else: 
        print("Error: Incorrect number of arguments")

