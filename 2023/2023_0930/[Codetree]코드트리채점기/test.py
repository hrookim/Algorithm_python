from queue import PriorityQueue


q = PriorityQueue()

q.put((1, 1, ""))
q.put((1, 2, ""))
q.put((3, 1, ""))
q.put((2, 10, ""))
q.put((1, 11, ""))
q.put((3, 2, ""))

print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.queue)