import json
from linked_list import LinkedList

# Specify the path to JSON file
json_file_path = r'checkpoint/big-tour-4-19/upper_bracket1.json'
file_encoding = 'utf-8'

# Read data from JSON file
with open(json_file_path, 'r', encoding=file_encoding) as json_file:
    data = json.load(json_file)

linkedlist = LinkedList()

for i, item in enumerate(data):
   linkedlist.insert(
       index=i+1,
       name=item.get('Name'),
       score=item.get('Score'),
       kills=item.get('Kills')
   )

linkedlist.display()
linkedlist.export_to_excel('upper_bracket1')
linkedlist.export_to_csv('upper_bracket1')