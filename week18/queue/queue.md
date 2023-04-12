# Queues

- FIFO
  - First in first out
- Benefits over vector, array: speed, memory efficency, dynamic sizing
- enqueue: add to queue
- dequeue: remove to queue
- Back: end to add to

```
T: float

class Entry:
  content: T
  next: *Entry

  Entry(): content(default of T), next(null)
  Entry(content, next)

class Queue:
  first: *Entry
  back: *Entry
  size: long (usize_t)

  Queue(): first(null), back(null), size(0)
  enqueue()
  dequeue()
  peek()

  dump()
```