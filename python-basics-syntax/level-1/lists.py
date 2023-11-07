
#lists are python arrays
list = [1,2,3.5,'abc']
print(list)
print(len(list))

#lists are mutable
list[0] = 'abc'
print(list)

#append
list.append(5)
print(list)

#extend
list.extend([1,2,3])
print(list)

# list.pop()
#inplace reverse
list.reverse()

#sort
#list.sort()

#list comprehension
mat = [[1,2],[3,4],[5,6]]
a = [row[0] for row in mat]
print(a)