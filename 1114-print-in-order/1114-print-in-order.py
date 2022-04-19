class Foo:
    def __init__(self):
        self.first_finished = False
        self.second_finished = False


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        
        self.first_finished = True


    def second(self, printSecond: 'Callable[[], None]') -> None:
        while not self.first_finished:
            pass
        
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        
        self.second_finished = True


    def third(self, printThird: 'Callable[[], None]') -> None:
        while not self.second_finished:
            pass
        
        # printThird() outputs "third". Do not change or remove this line.
        printThird()