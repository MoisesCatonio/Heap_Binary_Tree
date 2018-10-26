import Heap as hp

a = hp.element(2)
b = hp.element(3)
c = hp.element(4)
d = hp.element(5)
e = hp.element(6)
f = hp.element(7)

new_tree = hp.heap()

new_tree.add_element(c)
new_tree.add_element(a)
new_tree.add_element(b)
new_tree.add_element(d)
new_tree.add_element(e)
new_tree.add_element(f)

#new_tree.heapify()

new_tree.printer_list()

#new_tree.test()