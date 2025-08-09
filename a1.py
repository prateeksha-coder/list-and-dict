lst = ['Apple', 'Guava', 'Mango', 'Banana', 'Kiwi']

print("Length of list:", len(lst))
print("First Element:", lst[0])
print("Last Element:", lst[-1])

lst.append('Papaya')
print("Updated List :", lst)

lst.insert(2,"Watermelon")
print("Updated List :", lst)

lst.remove('Guava')
print("Updated List :", lst)

lst.sort()#ascending order
print("Sorted List:", lst)

lst.sort(reverse=True)#descending order
print("Sorted List:", lst)

lst.pop(1)
print("Updated List :", lst)

lst.reverse()
print("Reversed List :", lst)

print("Multiplication on List :", lst*2)

lst = lst[:5]#lst[start_index:end_index+1]
print("Sliced List :", lst)

lst.clear()
print("Updated List :", lst)
