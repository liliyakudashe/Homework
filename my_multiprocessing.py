from multiprocessing import Process, Manager, Pipe


class WarehouseManager:
    def __init__(self):
        self.data = Manager().dict()
        self.a, self.b = Pipe()

    def process_request(self, request):
        product, action, quantity = request
        if action == 'receipt':
            if product in self.data:
                self.data[product] += quantity
            else:
                self.data[product] = quantity
        elif action == 'shipment':
            if product in self.data:
                if self.data[product] >= quantity:
                    self.data[product] -= quantity
                else:
                    print(f'Отгружаем всё, что есть')
                    self.data[product] = 0
            else:
                print(f'Нельзя отгрузить {product}')

    def run(self, requestss):
        processes = []
        for request in requestss:
            process = Process(target=self.process_request, args=(request,))
            processes.append(process)
            process.start()
        for process in processes:
            process.join()


if __name__ == '__main__':
    manager = WarehouseManager()

    # Множество запросов на изменение данных о складских запасах
    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ]

    # Запускаем обработку запросов
    manager.run(requests)

    # Выводим обновленные данные о складских запасах
    print(manager.data)

