import easyocr
import cv2
import matplotlib.pyplot as plt
import pandas as pd
import os
from tqdm import tqdm

# List of languages to recognize
languages = ['en', 'th']

#Create reader from easyocr
reader = easyocr.Reader(languages, gpu=False)
img_size = (410, 555)

#Draw ractangle
def draw_rec(img, txt, pos, rgb):
     cv2.rectangle(img, pos[0], pos[2], rgb, 2)
     cv2.putText(
         img,
         txt,
         (pos[0][0] + 20, pos[0][1] + 40),
         cv2.FONT_HERSHEY_SIMPLEX,
         0.5,
         rgb,
         2,
         cv2.LINE_AA
    )

#combine split text
def combine_txt(data):
    unnessary_element = []
    for i, txt in enumerate(data):
        if (i % 2) == 1 and (txt[1][1] - data[i-1][1][1]) <= 5:
            unnessary_element.append(i)
            data[i-1][0] += f' {txt[0]}'
    return unnessary_element

class TextExtraction:
    def __init__(self):
        self.__PLAYER_NAME_THRESHOLD = 140
        self.__KILLS_THRESHOLD = 350

    def extract_text(self, folder: str, destination: str):
        #Define path to imge folder 
        for root, dirs, file_names in os.walk(folder):
            # Define the total number of iterations
            total_iterations = len(file_names)

            # Create a tqdm instance with the total number of iterations
            progress_bar = tqdm(total=total_iterations, desc="Processing", unit="iteration")
            
            for file_name in file_names: #Iterate over each file name in folder
                img = cv2.imread(folder + '/' + file_name) # Open image
                img = cv2.resize(img, img_size) #Resize image
                results = reader.readtext(img) # Get the results
                text = []
                kills = []

                #Define plyer name and kills
                for i, data in enumerate(results):
                    bbox, txt, score = data
                    bbox[0] = [int(x) for x in bbox[0]]
                    bbox[2] = [int(x) for x in bbox[2]]
                    
                    #Check if location is in the player name area
                    try:
                        if bbox[0][0] > self.__PLAYER_NAME_THRESHOLD and bbox[0][0] < self.__KILLS_THRESHOLD: #and is_elf_lvl(i, txt):
                            draw_rec(img, txt, bbox, (0, 255, 0))
                            text.append([txt, bbox[0]])
                    except:
                        print("An exception occurred")
            
                    #Check if location is in the kills area
                    try:
                        if bbox[0][0] > self.__KILLS_THRESHOLD:
                            draw_rec(img, txt, bbox, (255, 0, 0))
                            kills.append(txt)
                    except:
                        print("An exception occurred")

                # print('-' * 200)
                # print(' '*20 + file_name + ' '*20)

                try:
                    rm_element = combine_txt(text)
                    [text.pop(i) for i in rm_element]
                except:
                    print(f'some index out of range at {file_name}')

                player_name = []
                for i in range(len(text)):
                    if (i % 2) == 0:
                        player_name.append(text[i][0])


                player_info = {
                    'name': player_name,
                    'score': [8, 6, 5, 4, 3, 2, 1, 0],
                    'kills': kills
                }

                # print(player_info)

                # Create data frame
                try:
                    df = pd.DataFrame(player_info)
                    df.to_csv(destination + file_name.split()[0] + '.csv', index=True, index_label="index")
                    df.to_excel('output/' + file_name.split()[0] + '.xlsx', index=True, index_label="index")
                    # print(df)
                except:
                    print('Player and kills must have the same length')

                #Update the progress bar
                progress_bar.update(1)
            
            progress_bar.close()