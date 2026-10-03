from collections import deque

fila = deque(["item1","item2","item3"])
#LIFO
fila.append("item4")
#FIFO
fila.appendleft("item0")
print(fila)

fila.pop()
print(fila)
fila.popleft()
print(fila)