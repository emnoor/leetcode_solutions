import queue


class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_q = queue.Queue()
        self.bar_q = queue.Queue()
        self.foo_q.put(1)

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.foo_q.get()
            printFoo()
            self.bar_q.put(1)

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.bar_q.get()
            printBar()
            self.foo_q.put(1)