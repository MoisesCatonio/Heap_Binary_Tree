class element:
    def __init__(self, data=None, own_pos=None, father=None, left_son=None, right_son=None):
        self.data = data
        self.father = father
        self.own_pos = own_pos
        self.left_son = left_son
        self.right_son = right_son

class heap:
    def __init__(self):
        self.tree = []

    def determine_positions(self):
        for i in range(0, len(self.tree)):
            self.tree[i].own_pos = i
            self.tree[i].left_son = int(2*i+1)
            self.tree[i].right_son = int(2*i+2)
            if(i != 0):
                self.tree[i].father = int((i-1)/2)
            else:
                self.tree[i].father = None

    def add_element(self, new_element):
        self.tree.append(new_element)
        self.determine_positions()

    def swap(self, elem1, elem2):
        aux = self.tree[elem1.own_pos]
        self.tree[elem1.own_pos] = self.tree[elem2.own_pos] 
        self.tree[elem2.own_pos] = aux
        self.determine_positions()

    def heapify(self):
        last_elem = len(self.tree)-1
        for last_1 in range(last_elem, 0, -1):
            for last in range(last_elem, 0, -1):
                if(last > 1):
                    iter2 = last - 1
                    if(self.tree[last].father == self.tree[iter2].father):
                        min_value = min(self.tree[last].data, self.tree[iter2].data)
                        if(self.tree[last].data == min_value):
                            elem_change = self.tree[last]
                        else:
                            elem_change = self.tree[last-1]
                        if(min_value<self.tree[elem_change.father].data):
                            self.swap(elem_change, self.tree[elem_change.father])
                    else:
                        elem_change = self.tree[last]
                        if(elem_change.data < self.tree[elem_change.father].data):
                            self.swap(elem_change, self.tree[elem_change.father])
                        
    def printer_list(self):
        for i in range(0,len(self.tree)):
            print(str(self.tree[i].data) + ", ")
