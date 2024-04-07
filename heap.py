import heapq

a = [1,4,2,3,4,5,6,7,8]
heapq.heapify(a)
print(list(a))

#insert
heapq.heappush(a,15)
print(list(a))

#Delete
print(heapq.heappop(a))

print(heapq.heappushpop(a,2))
print(heapq.heapreplace(a,10))
max


#Rresentation of binary tree with array
#index one
#element and relation of element
#2*i,-left child
#2*i+1 -right
#[1/2]-parent at
