from threading import Semaphore, Barrier


class H2O:
    def __init__(self):
        self.sem_o = Semaphore(1)
        self.sem_h = Semaphore(2)
        self.bar = Barrier(3)

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.sem_h.acquire()
        self.bar.wait()
        
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        
        self.sem_h.release()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.sem_o.acquire()
        self.bar.wait()
        
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        
        self.sem_o.release()