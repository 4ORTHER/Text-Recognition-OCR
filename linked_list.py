class Node:
        def __init__(self, index, name, kills):
                self.index = index
                self.name = name
                self.kills = kills
                self.score = 0
                self.next_node = None

class SinglyLinkedList:
        def __init__(self):
                self.head_node = None

        def print_list(self):
                node = self.head_node
                while node is not None:
                        print(f'{node.id}|{node.name}|{node.kills}|{node.score}')
                        node = node.next_node