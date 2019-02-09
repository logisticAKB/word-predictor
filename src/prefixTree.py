class TreeNode:
    def __init__(self, data=None, children=None, is_key=None):
        self.data = data
        self.children = children
        self.is_key = is_key

    def set_data(self, data):
        self.data = data

    def add_children(self, child):
        self.children.append(child)

    def set_key(self, is_key):
        self.is_key = is_key


class PrefixTree:
    def __init__(self):
        self.root = TreeNode("", [], False)

    def insert_word(self, word):
        cur_node = self.root
        for i in range(len(word)):
            new_node = self.node_has_child(cur_node, word[i])
            if new_node:
                new_node.set_key(i == len(word) - 1)
            else:
                new_node = TreeNode(word[i], [], i == len(word) - 1)
                cur_node.add_children(new_node)
            cur_node = new_node

    def node_has_child(self, node, value):
        for child in node.children:
            if child.data == value:
                return child
        return None


pt = PrefixTree()
file = open("dictionary.txt", "r")
for line in file:
    word = line.strip()
    pt.insert_word(word)

file.close()
