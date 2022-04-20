from queue import Queue


class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.fizz_q = Queue()
        self.buzz_q = Queue()
        self.fizzbuzz_q = Queue()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while True:
            v = self.fizz_q.get()
            if v is None:
                self.fizz_q.task_done()
                break
            printFizz()
            self.fizz_q.task_done()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while True:
            v = self.buzz_q.get()
            if v is None:
                self.buzz_q.task_done()
                break
            printBuzz()
            self.buzz_q.task_done()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while True:
            v = self.fizzbuzz_q.get()
            if v is None:
                self.fizzbuzz_q.task_done()
                break
            printFizzBuzz()
            self.fizzbuzz_q.task_done()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n+1):
            if i % 15 == 0:
                self.fizzbuzz_q.put(1)
                self.fizzbuzz_q.join()
            elif i % 3 == 0:
                self.fizz_q.put(1)
                self.fizz_q.join()
            elif i % 5 == 0:
                self.buzz_q.put(1)
                self.buzz_q.join()
            else:
                printNumber(i)
        
        self.fizz_q.put(None)
        self.buzz_q.put(None)
        self.fizzbuzz_q.put(None)
        self.fizz_q.join()
        self.buzz_q.join()
        self.fizzbuzz_q.join()