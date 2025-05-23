from queue import Queue
import random
import time


request_queue = Queue()

# Для генерації заявок
def generate_request():
    request_id= random.randint(1, 5555)
    request_data = f"Request №{request_id}"
    request_queue.put(request_data)
    print(f"Add: {request_data}")


# Для обробки заявок
def process_request():
    if not request_queue.empty():
        request_data = request_queue.get()
        print(f"Обробляємо заявку: {request_data}")
        time.sleep(2)
        print(f"Завершено обробляти заявку: {request_data}")
    else:
        print("Черга порожня, зачеайте...")
        time.sleep(1)

#  Для запуску програми(use hint)
while True:
    go_pro_queue = input("Введіть 'go' для генерації заявки або 'proces' для обробки заявки,  'exit' для виходу: ")

    if go_pro_queue == "go":
        generate_request()
    elif go_pro_queue == "proces":
        process_request()
    elif go_pro_queue == "exit":
        print("Завершуємо! Дякую! Виходимо...")
        break
    else:
        print("Невірна команда, вводьте англійськими літерами: go, proces, exit")
    
    time.sleep(2)






