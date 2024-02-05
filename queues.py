import queue
import threading
import time


class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False


class Cafe:
    def __init__(self, tables):
        self.queue = queue.Queue()
        self.tables = tables

    def customer_arrival(self):
        for i in range(1, 21):
            print(f"Посетитель номер {i} прибыл")
            customer = threading.Thread(target=self.serve_customer, args=(i,))
            customer.start()
            time.sleep(1)

    def serve_customer(self, customer_number):
        for table in self.tables:
            if not table.is_busy:
                table.is_busy = True
                print(f"Посетитель номер {customer_number} сел за стол {table.number}")
                time.sleep(5)
                print(f"Посетитель номер {customer_number} покушал и ушёл.")
                table.is_busy = False
                break
        print(f"Посетитель номер {customer_number} ожидает свободный стол.")
        self.queue.put(customer_number)


class Customer(threading.Thread):
    def __init__(self, cafe):
        super().__init__()
        self.cafe = cafe

    def run(self):
        while True:
            if not self.cafe.queue.empty():
                customer_number = self.cafe.queue.get()
                for table in self.cafe.tables:
                    if not table.is_busy:
                        table.is_busy = True
                        print(f"Посетитель номер {customer_number} сел за стол {table.number}")
                        time.sleep(5)
                        print(f"Посетитель номер {customer_number} покушал и ушёл.")
                        table.is_busy = False
                        break


table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

cafe = Cafe(tables)

customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

customer_arrival_thread.join()
