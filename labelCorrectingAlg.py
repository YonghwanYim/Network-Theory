"""
* Author : Yonghwan Yim
* Title : Label Correcting Algorithm using FIFO queue and Dequeue
* Subject : IE535 network theory and applications
"""

from collections import deque

class LabelCorrectingAlgorithm:
    def __init__(self, vertices, arcs, start, use_fifo=True):
        self.vertices = vertices
        self.graph = {i: [] for i in range(1, vertices + 1)}
        self.use_fifo = use_fifo

        for u, v, weight in arcs:
            self.graph[u].append((v, weight))

        self.d = [float('inf')] * (vertices + 1)
        self.pred = [float('inf')] * (vertices + 1)
        self.visit = [0] * (vertices + 1)

        self.d[start] = 0
        self.pred[start] = 0
        self.visit[start] = 1

        if self.use_fifo:
            self.queue = [start]
        else:
            self.deque_obj = deque([start])

    def run_algorithm(self):
        label_updates = 0

        while self.queue_or_deque:
            current = self.get_next_node()

            for neighbor, weight in self.graph[current]:
                if self.d[current] + weight < self.d[neighbor]:
                    self.d[neighbor] = self.d[current] + weight
                    self.pred[neighbor] = current
                    label_updates += 1
                    self.update_queue_or_deque(neighbor)

        return self.d[1:], self.pred[1:], label_updates

    def get_next_node(self):
        if self.use_fifo:
            return self.queue.pop()
        else:
            return self.deque_obj.popleft()

    def update_queue_or_deque(self, neighbor):
        if self.use_fifo:
            if neighbor not in self.queue:
                self.queue.append(neighbor)
        else:
            if neighbor not in self.deque_obj:
                if self.visit[neighbor] == 0:
                    self.deque_obj.append(neighbor)
                    self.visit[neighbor] = 1
                else:
                    self.deque_obj.appendleft(neighbor)

    @property
    def queue_or_deque(self):
        if self.use_fifo:
            return bool(self.queue)
        else:
            return bool(self.deque_obj)

vertices = 7
arcs = [(1, 2, 6), (1, 3, 2), (2, 3, -5), (2, 4, -1), (2, 5, 4),
        (3, 4, 3), (3, 6, -6), (4, 5, 4), (5, 7, -7), (6, 4, 1), (6, 7, 7)]
start_node = 1

# Use FIFO algorithm
fifo_algorithm = LabelCorrectingAlgorithm(vertices, arcs, start_node, use_fifo=True)
labels_fifo, pred_fifo, updates_fifo = fifo_algorithm.run_algorithm()

# Use dequeue algorithm
deque_algorithm = LabelCorrectingAlgorithm(vertices, arcs, start_node, use_fifo=False)
labels_deque, pred_deque, updates_deque = deque_algorithm.run_algorithm()

print("[ FIFO ]")
print("# of Updates:", updates_fifo)
print("Final value of Labels:", labels_fifo)
print("Final pred of Labels:", pred_fifo)

print("\n[ Dequeue ]")
print("# of Updates:", updates_deque)
print("Final value of Labels:", labels_deque)
print("Final pred of Labels:", pred_deque)
