class element:
    def __init__(self, data=None, left_son=None, right_son=None):
        self.data = data
        self.left_son = left_son
        self.right_son = right_son

class heap:
    def __init__(self):
        self.tree = []
    
    def add_element(self, element, dad_data):
        if(len(self.tree) > 0):
            for i in range(0,len(self.tree)):
                if(dad_data == self.tree[i].data):
                    if(self.tree[i].left_son == None):
                        self.tree[i].left_son = 2*i+1
                        self.tree.insert(2*i+1, element)
                        break
                    elif(self.tree[i].right_son == None):
                        self.tree[i].right_son = 2*i+2
                        self.tree.insert(2*i+2, element)
                        break
                    else:
                        print("The element found, already have two sons! Aborting Operation!")
                        break
        else:
            self.tree.append(element)
    
    def get_dado(self, position):
        return print(self.tree[position].data)

a = element(2)
b = element(3)
c = element(4)
d = element(5)

new_tree = heap()

new_tree.add_element(a, 0)
new_tree.add_element(b, 2)
new_tree.add_element(c, 2)
new_tree.add_element(d, 2)

new_tree.get_dado(1)
new_tree.get_dado(2)