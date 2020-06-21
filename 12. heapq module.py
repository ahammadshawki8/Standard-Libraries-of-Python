# heapq library

# heap is one kind of a priority queue data structure.
# it is a binary tree implementation of priority queue
# where each values are ordered by the key.

# python has a built in library which is called heapq to work with heap data structures

# first lets import the heapq library.
import heapq

# lets see the all functions of heapq module.
print(dir(heapq))

# we can se that we have-
['__about__', '__all__', '__builtins__', '__cached__', '__doc__', '__file__',
 '__loader__', '__name__', '__package__', '__spec__', '_heapify_max',
 '_heappop_max', '_heapreplace_max', '_siftdown', '_siftdown_max', '_siftup',
 '_siftup_max', 'heapify', 'heappop', 'heappush', 'heappushpop', 'heapreplace',
 'merge', 'nlargest', 'nsmallest']

# lets see what the public methods do.
# first lets define a heap. It is basically a list of python.
heap = []

# now lets add couple of key-value pairs to our list using heappush() method
heapq.heappush(heap,(9,"a"))
heapq.heappush(heap,(0,"b"))
heapq.heappush(heap,(6,"c"))
heapq.heappush(heap,(8,"d"))
heapq.heappush(heap,(4,"e"))
heapq.heappush(heap,(2,"f"))
heapq.heappush(heap,(5,"g"))
print(heap)

# now lets delete the smallest key-value pair from the heap using heappop() method.
small = heapq.heappop(heap)
print(small)
print(heap)
# do that again-
small = heapq.heappop(heap)
print(small)
print(heap)

# now lets add a value to the heap and then pop a value from it.
# we can do that by heappushpop() method.
small=heapq.heappushpop(heap,(0,"p"))
print(small)
print(heap)
# do that again-
small=heapq.heappushpop(heap,(8,"t"))
print(small)
print(heap)

# we can do the same operation by heappreplace() method.
small=heapq.heappushpop(heap,(0,"k"))
print(small)
print(heap)
# do that again-
small=heapq.heappushpop(heap,(3,"n"))
print(small)
print(heap)

# the difference between heappushpop() and heappreplace() is:
# in heappushpop() the pop being performed after the push.
# in heappreplace() the pop being performed before the push (in other words, the new
# element cannot be returned as the smallest).

# we can transform a unordered list to a heap using heapify() method.
unordered = [(2,"k"),(0,"g"),(1,"f")]
heapq.heapify(unordered)
print(unordered)

# we can print first n-th largest pair from the heap using nlargest() method.
print(heapq.nlargest(3,heap))
# we can print first n-th smallest pair from the heap using nsmallest() method.
print(heapq.nsmallest(2,heap))

# we can merge two heap and make them one.
merged = list(heapq.merge(heap,unordered)) # NOTE that we have to convert it to list.
print(merged)

