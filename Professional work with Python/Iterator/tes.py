class HelloWorldIterator:
    def __init__(self, n):
        self.n = n
    def __iter__(self):
        print('Цикл начинается')
        self.counter = 0
        return self
    def __next__(self):
        self.counter += 1
        if self.counter > self.n:
            print('Цикл завершается')
            raise StopIteration
        return self.counter


for item in HelloWorldIterator(n=3):
    print(item)