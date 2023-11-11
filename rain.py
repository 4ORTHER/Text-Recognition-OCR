import json
from linked_list import LinkedList
import os

folder = r'checkpoint/big-tour-4-19/knock-out/'

for root, dirs, file_names in os.walk(folder):
    for file_name in file_names:
        file_encoding = 'utf-8'
        path = folder + file_name

        _, file_extension = os.path.splitext(path)
        if file_extension.lower() != '.json':
            print("Skipping non-JSON file:", path)
            continue  # Skip to the next iteration of the loop

        # print(path)

        # Read data from JSON file
        with open(path, 'r', encoding=file_encoding) as json_file:
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
        linkedlist.export_to_excel(file_name)
        linkedlist.export_to_csv(file_name)