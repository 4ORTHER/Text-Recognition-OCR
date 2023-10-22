from text_extraction import TextExtraction
from linked_list import LinkedList
import os
import pandas as pd

def insert_csv_to_linked_list(folder: str, linked_list: LinkedList):
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
                    try:
                         linked_list.insert(
                            index=0,
                            name=data[1].strip(),
                            score=int(data[2]),
                            kills=int(data[3])
                        )
                    except:
                         print('wrong type to convert')

def extract_text(source: str, destination: str):
    text_extraction = TextExtraction()
    text_extraction.extract_text(source, destination)

destination1 = r'extracted_text/mini-tour-21-22/'
# destination2 = r'extracted_text/mini-tour-21-22/Game2'

extract_text(r'images/mini-tour-21-22/Final/', destination1)
# extract_text(r'images/DOW-mini-tour-30/game2/', destination2)


# results = LinkedList()
# insert_csv_to_linked_list(destination1, results)
# results.display()
# results.export_to_csv('summary')
# results.export_to_excel('summary')