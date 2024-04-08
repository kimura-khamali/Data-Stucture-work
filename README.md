#Heap

It is a complete tree binary data structure which satisfy heap properties.
Min-Value of children is less than or equal to its own value equal
Opposite to max-Value

Advantage  
Efficient for insertion and deletion.
Has efficient priority queues.
Guarantee success for both minimum and maximum.



Disadvantages
Lack of Flexibility.
It’s not ideal for searching.
It’s not a stable data structure.
It is complex
It has a static memory management.


Property
It’s Binary Tree is always complete.
It follows the heap property of maximum and minimum.


Adding in Heaps
 

When an element is added its place in the leaf part of the element to the right side.
Using Max
 If the no. is more than the previous no. it  compares with the previous number using the flow value which
i/2  and it moves to the next level.

This is till it reaches a number that does not contrast it anymore


Removing in Heaps
When removing an element or number only the root or main element is removed.
 Using Max
The number is removed.
The leaf number  is placed as the root element .
The check begins checking if the number is less or more than the numbers below.
If it's more it remains.
If its less it has to be replaced by the lower one until it all  fits from the greatest to lowest
i*2
i*2+1

Accessing Heaps

When accessing heaps we use
i= to the index of the element which begins from one
2*i=  to know the left child in a binary tree
2*i+1= to know the right child 

[1/2] = To access the parent value or the root value.   []
Is the flowvalue

Import heapq

heapq.heappush= add
heapq.heappop= remove
heapq.heapreplace
