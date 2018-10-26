import Heap as hp

a = hp.element(2)

b = hp.element(5)#filho do 2
c = hp.element(4)#filho do 2

d = hp.element(7)#filho do 5
e = hp.element(6)#filho do 5

f = hp.element(3)#filho do 4
g = hp.element(10)#filho do 4
new_tree = hp.heap()

new_tree.add_element(a)
new_tree.add_element(b)
new_tree.add_element(c)
new_tree.add_element(d)
new_tree.add_element(e)
new_tree.add_element(f)
new_tree.add_element(g)

new_tree.heapify()

new_tree.printer_list()

#new_tree.test()