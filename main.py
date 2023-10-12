from text_extraction import TextExtraction
from linked_list import LinkedList
import os
import pandas as pd

def create_linked_list(folder: str, linked_list: LinkedList):
        # Iterate through files in the folder
        for filename in os.listdir(folder):
            if filename.endswith('.csv'):  # Check if the file is a CSV file
                file_path = os.path.join(folder, filename)
                
                # Read the CSV file into a pandas DataFrame without considering the first row as column names
                df = pd.read_csv(file_path, header=None)
                df.columns = df.loc[0]
                df = df.drop(0)

                # Iterate through rows in the DataFrame and insert data into the linked list
                for _, row in df.iterrows():
                    data = row.values
                    linked_list.insert(
                         index=int(data[0]) + 1,
                         name=data[1].strip(),
                         kills=int(data[2])
                    )

path_folder = r'images/DOW-mini-tour-30/Game1/'
destination_folder = r'extracted_text/Game1/'

text_extraction = TextExtraction()

# text_extraction.extract_text(path_folder, destination_folder)
game1 = LinkedList()
create_linked_list(destination_folder, game1)
game1.display()
game1.export_to_csv('game1')
