import Heap as hp

a = hp.element(2)#(Stay in place)

b = hp.element(5)#filho do 2 (Stay in place)
c = hp.element(4)#filho do 2 (Have to switch with 3)

d = hp.element(7)#filho do 5 (Stay in place)
e = hp.element(6)#filho do 5 (Stay in place)

f = hp.element(3)#filho do 4 (Have to switch with 4)
g = hp.element(10)#filho do 4 (Stay in place)
new_tree = hp.heap()


#Switch and play with the positions, to test the different configurations.
new_tree.add_element(g)
new_tree.add_element(b)
new_tree.add_element(c)
new_tree.add_element(e)
new_tree.add_element(d)
new_tree.add_element(f)
new_tree.add_element(a)

print("Before heapify")
new_tree.printer_list()
print("")

new_tree.heapify()
print("After heapify")
new_tree.printer_list()
