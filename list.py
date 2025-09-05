'''
print(friend[0])
friend[0] = "Ratan"
print(friend)

friend = ["Rolf", "Bob", "Jen", 45, 67.8, True ]
friend[2]="feb"
print(friend[2])

list = [3, 5, 2, 4, 1]
print("Original",list )
list.sort()
print("Sort",list )
list.reverse()
print("reverse",list )
list.append(6)
print("Append",list )
list.insert(0, 9)
print("Inset",list )
list.remove(3)  
print("Remove",list )
li = [3, 5, 2, 4, 1]
value = li.pop(3)
print("Pop",value)
print(li.pop(3))

'''
a = (1,)
print(type(a))