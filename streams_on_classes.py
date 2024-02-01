import threading
import time


class Knight(threading.Thread):
    def __init__(self, name_knight, skill):
        super().__init__()
        self.name_knight = name_knight
        self.skill = skill

    def run(self):
        print(f'{self.name_knight} на нас напали!')
        count = 100
        days = 0
        while count > 0:
            days += 1
            count -= self.skill
            if count < 0:
                count = 0
            print(f'{self.name_knight}, сражается {days} день(дня)..., осталось {count} воинов.')
            time.sleep(1)
        print(f'{self.name_knight} одержал победу спустя {days} дней!')


knight1 = Knight("Sir Lancelot", 10)
knight2 = Knight("Sir Galahad", 20)

knight1.start()
knight2.start()

knight1.join()
knight2.join()

print("Все битвы закончились!")
