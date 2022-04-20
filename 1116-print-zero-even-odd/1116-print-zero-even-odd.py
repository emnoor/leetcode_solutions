from queue import Queue


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.zero_q = Queue()
        self.zero_q.put(1)
        self.other_qs = [Queue(), Queue()]

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n+1):
            self.zero_q.get()
            printNumber(0)
            self.other_qs[i % 2].put(1)
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n+1, 2):
            self.other_qs[0].get()
            printNumber(i)
            self.zero_q.put(1)
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n+1, 2):
            self.other_qs[1].get()
            printNumber(i)
            self.zero_q.put(1)
