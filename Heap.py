class element:
    def __init__(self, data=None, father=None, left_son=None, right_son=None):
        self.data = data
        self.father = father
        self.left_son = left_son
        self.right_son = right_son

class heap:
    def __init__(self):
        self.tree = []

    def determine_positions(self):
        for i in range(0, len(self.tree)):
            self.tree[i].left_son = 2*i+1
            self.tree[i].right_son = 2*i+2
            if(i != 0):
                self.tree[i].father = (i-1)/2
            else:
                self.tree[i].father = None
                
    def add_element(self, new_element):
        self.tree.append(new_element)
        self.determine_positions()

    def swap(self, elem1, elem2):
        aux = elem1
        elem1 = elem2
        elem2 = aux

    def get_dado(self, position):
        return self.tree[position].data
    
    def printer_list(self):
        for i in range(0,len(self.tree)):
            print(str(self.tree[i].data) + ", ")