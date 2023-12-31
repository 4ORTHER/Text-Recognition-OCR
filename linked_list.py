import pandas as pd

class Node:
        def __init__(self, index: int, name: str, score: int, kills: float):
                self.index = index
                self.name = name
                self.score = score
                self.kills = kills
                self.next_node = None

class LinkedList:
        def __init__(self):
                self.head_node = None

        def display(self):
                node = self.head_node
                print('-'*200)
                while node:
                        print(f'{node.index}|{node.name}|{node.score}|{node.kills}')
                        node = node.next_node
                print('-'*200)

        # Method to insert data into the linked list
        def insert(self, index: int, name: str, score: int, kills: float):
                new_node = Node(index, name, score, kills)
                if self.head_node is None:
                        self.head_node = new_node
                else:
                        current = self.head_node
                        while current.next_node:
                                if current.name == new_node.name:
                                        current.score += new_node.score  # Add score if name is the same
                                        current.kills += new_node.kills  # Add kills if name is the same
                                        return
                                current = current.next_node
                        if current.name == new_node.name:
                                current.score += new_node.score  # Add score if name is the same
                                current.kills += new_node.kills  # Add kills if name is the same
                        else:
                                current.next_node = new_node
                self.sort()

        def sort(self):
                if self.head_node is None or self.head_node.next_node is None:
                        return

                swapped = True
                while swapped:
                        swapped = False
                        current = self.head_node
                        while current.next_node:
                                if current.score < current.next_node.score or (current.score == current.next_node.score and current.kills < current.next_node.kills):
                                        current.name, current.next_node.name = current.next_node.name, current.name
                                        current.score, current.next_node.score = current.next_node.score, current.score
                                        current.kills, current.next_node.kills = current.next_node.kills, current.kills
                                        swapped = True
                                current = current.next_node

        def export_to_csv(self, filename: str):
                data = []
                current = self.head_node
                while current:
                        data.append([current.name, current.score, current.kills])
                        current = current.next_node

                df = pd.DataFrame(data, columns=['Name', 'Score', 'Kills'])
                df.to_csv('output/' + filename + '.csv', index=True, index_label='index')

        def export_to_excel(self, filename: str):
                data = []
                current = self.head_node
                while current:
                        data.append({'Index': current.index,'Name': current.name, 'Score': current.score, 'Kills': current.kills})
                        current = current.next_node
                df = pd.DataFrame(data)
                df.to_excel('output/' + filename + '.xlsx', index=False)
