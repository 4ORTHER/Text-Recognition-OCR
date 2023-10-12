score_dict = {
        1: 8,
        2: 6,
        3: 5,
        4: 4,
        5: 3,
        6: 2,
        7: 1,
        8: 0
}

class Node:
        def __init__(self, index: int, name: str, kills: int):
                self.index = index
                self.name = name
                self.kills = kills
                self.score = score_dict.get(index)
                self.next_node = None

class LinkedList:
        def __init__(self):
                self.head_node = None

        def display(self):
                node = self.head_node
                while node:
                        print('-'*200)
                        print(f'{node.index}|{node.name}|{node.kills}|{node.score}')
                        node = node.next_node

        # Method to insert data into the linked list
        def insert(self, index: int, name: str, kills: int):
                new_node = Node(index, name, kills)
                if self.head_node is None:
                        self.head_node = new_node
                else:
                        current = self.head_node
                        while current.next_node:
                                current = current.next_node
                        current.next_node = new_node