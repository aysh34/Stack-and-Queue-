# A simple queue implementation using a list
class Queue:
    def __init__(self):
        self.queue = []

    # Enqueue: Add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # Dequeue: Remove an item from the front of the queue
    def dequeue(self):
        if not self.isEmpty():
            return self.queue.pop(0)  # Remove the first item
        else:
            return "Queue is empty"

    # Peek/Front: See the front item of the queue
    def peek(self):
        if not self.isEmpty():
            return self.queue[0]  # Return the first item
        else:
            return "Queue is empty"

    # isEmpty: Check if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.dequeue())
print(q.queue)
