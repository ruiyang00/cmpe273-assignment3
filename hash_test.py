
from DoubleLinkedlist import DoubleLinkedlist


list = DoubleLinkedlist()
data1 = {'name': 'Brad Pitt', 'email': 'bpitt@gmail.com', 'age': 30}
data2 = {'name': 'Wall Bran', 'email': 'wbran@gmail.com', 'age': 18}
data3 = {'name': 'Robert Jennifer', 'email': 'rjennifer@gmail.com', 'age': 24}


list.addFront(data1)
list.addFront(data2)
list.addFront(data3)

head = list.head.next.value
print(head)
print(list.get_size())
