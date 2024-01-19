class EvenNumbers:
    def __init__(self, start=0, end=1):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start % 2 == 0:
            result = self.start
        else:
            result = self.start + 1

        if result >= self.end:
            raise StopIteration

        self.start += 2

        return result


even_numbers = EvenNumbers(2, 10)
for num in even_numbers:
    print(num)
