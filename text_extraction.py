import easyocr
import cv2
import matplotlib.pyplot as plt
import pandas as pd
import os

#Create reader from easyocr
reader = easyocr.Reader(['en', 'th'], gpu=False)

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
     
#Find elf lvl text using recursive
def find_elf_lvl(i, data, threshold):
    if i <= 0:
        return
    
    next_i = i - 1

    if (int(data[i][1][1]) - int(data[next_i][1][1])) >= threshold:
        data[i][0] = True

    find_elf_lvl(next_i, data, threshold)

#combine split text
def combine_txt(data):
    for i, txt in enumerate(data):
        txt = txt.strip()
        if txt[0] == 'i' and txt[-1] == ']':
            data[i:i+2] = [''.join(data[i:i+2])]

class TextExtraction:
    def __init__(self, folder, destination):
        self.folder = folder
        self.destination = destination
        self.__PLAYER_NAME_THRESHOLD = 140
        self.__ELF_LVL_THRESHOLD = 35
        self.__KILLS_THRESHOLD = 350

    def extract_text(self):
        #Define path to imge folder 
        for root, dirs, file_names in os.walk(self.folder):
            for file_name in file_names: #Iterate over each file name in folder
                img = cv2.imread(self.folder + '/' + file_name) # Open image
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
                            kills.append(int(txt))
                    except:
                        print("An exception occurred")

                find_elf_lvl(len(text) - 1, text, self.__ELF_LVL_THRESHOLD)

                player_name = []
                for data in text:
                    if type(data[0]) == type('str'):
                        player_name.append(data[0])
                combine_txt(player_name)

                print('*'*20 + file_name + '*'*20)
                player_info = {
                    'name': player_name,
                    'kills': kills
                }

                # Create data frame
                df = pd.DataFrame(player_info)
                df.to_csv(self.destination + file_name.split()[0] + '.csv')
                print('-' * 200)
                print(df)