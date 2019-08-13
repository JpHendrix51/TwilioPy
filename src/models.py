from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Queue:

    def __init__(self, mode):
        self._queue = []
        # depending on the _mode, the queue has to behave like a FIFO or LIFO
        self._mode = mode

    def enqueue(self, item):
        self._queue.append(item)
        return True

    def dequeue(self):
        if self._mode == "FIFO":
            self._queue.pop(0)
            return self._queue
        else:
            return self._queue.pop(-1)

    def get_queue(self):
        return self._queue
    def size(self):
        return len(self._queue)


