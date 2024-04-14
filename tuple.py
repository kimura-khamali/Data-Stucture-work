# count() number of occurrences

my_tuple = (1,2,3,4,5,6,7,8,2,3,4,2)
count = my_tuple.count(2)
print(count)

fruits = ("banana","Orange","mango","pineapple","Mango","mango")
count_words = fruits.count("mango")
print(fruits)
print(count_words)

print("Number of times 'mango' appears in the tuple: ", count_words)

# index() find occurence of the first index


my_tuple1 = (1,2,3,4,5,6,7,8,2,3,4,2)
occurrence = my_tuple1.index(2)
print(occurrence)

fruits1 = ("banana","Orange","mango","pineapple","Mango","mango")
index_words = fruits1.count("mango")
print(fruits1)
print(index_words)

print("'mango' appears in the tuple on index: ", index_words)

# functions in tuple
# len() -length
#  max() . maximum value in tuple
#  min()
# sum()
on_tuple = (1,2,3,4,4)
print(len(on_tuple))
print(max(on_tuple))
print(min(on_tuple))
print(sum(on_tuple))


my_list = [1,2,3,4,5,6]
m_tuple = tuple(my_list)
print(m_tuple)




