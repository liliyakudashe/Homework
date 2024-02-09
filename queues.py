import queue
import threading
import time


class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False
        self.lock = threading.Lock()


class Cafe:
    def __init__(self, tables):
        self.queue = queue.Queue()
        self.tables = tables

    def customer_arrival(self):
        customers = []
        for i in range(1, 21):
            time.sleep(1)
            print(f"Посетитель номер {i} прибыл", flush=True)
            customer = Customer(self, i)
            customers.append(customer)
            customer.start()
        for cust in customers:
            cust.join()

    def serve_customer(self, customer):
        for table in self.tables:
            with table.lock:
                if not table.is_busy:
                    print(f"Посетитель номер {customer.number} сел за стол {table.number}", flush=True)
                    table.is_busy = True
                    time.sleep(5)
                    table.is_busy = False
                    print(f"Посетитель номер {customer.number} покушал и ушёл", flush=True)
                    if not self.queue.empty():
                        next_customer = self.queue.get()
                        self.serve_customer(next_customer)
                    return
        print(f"Посетитель номер {customer.number} ожидает свободный стол", flush=True)
        self.queue.put(customer)


class Customer(threading.Thread):
    def __init__(self, cafe, number):
        super().__init__()
        self.cafe = cafe
        self.number = number

    def run(self):
        self.cafe.serve_customer(self)


table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

cafe = Cafe(tables)

customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

customer_arrival_thread.join()
