import easyocr
import cv2
import matplotlib.pyplot as plt
import pandas as pd
import os

# List of languages to recognize
languages = ['en', 'th']

# Create reader from easyocr
reader = easyocr.Reader(languages, gpu = False)

img_size = (410, 555)

# Define path of the image
img_name = '\Game1Group2.png'
# img_path = r'C:\Users\USER\Documents\GitHub\Text-recognition--OCR-\images\DOW-mini-tour-30\game1' + img_name
img_path = r'C:\Users\USER\Documents\GitHub\Text-recognition--OCR-\images\mini-tour-21-22' + img_name

# Open image
img = cv2.imread(img_path)

#Resize image
img = cv2.resize(img, img_size)

# Get the results
results = reader.readtext(img)

text = []
kills = []
PLAYER_NAME_THRESHOLD = 140
ELF_LVL_THRESHOLD = 35
KILLS_THRESHOLD = 350

#Draw ractangle
def draw_rec(img, pos, rgb):
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

# combine split text
def combine_txt(data):
    unnessary_element = []
    for i, txt in enumerate(data):
        if (i % 2) == 1 and (txt[1][1] - data[i-1][1][1]) <= 5:
            unnessary_element.append(i)
            data[i-1][0] += f' {txt[0]}'
    return unnessary_element

#Define plyer name and kills
for i, data in enumerate(results):
    bbox, txt, score = data

    bbox[0] = [int(x) for x in bbox[0]]
    bbox[2] = [int(x) for x in bbox[2]]
    
    # Check if location is in the player name area
    try:
        if bbox[0][0] > PLAYER_NAME_THRESHOLD and bbox[0][0] < KILLS_THRESHOLD: #and is_elf_lvl(i, txt):
            draw_rec(img, bbox, (0, 255, 0))
            text.append([txt, bbox[0]])
    except:
        print("An exception occurred")

    #Check if location is in the kills area
    try:
        if bbox[0][0] > KILLS_THRESHOLD:
            draw_rec(img, bbox, (255, 0, 0))
            kills.append(txt)
    except:
        print("An exception occurred")

try:
    rm_element = combine_txt(text)
    [text.pop(i) for i in rm_element]
except:
    print('some index out of range')

player_name = []
for i in range(len(text)):
    if (i % 2) == 0:
        player_name.append(text[i][0])

print(player_name)
print(kills)

player_info = {
    'name': player_name,
    'score': [8, 6, 5, 4, 3, 2, 1, 0],
    'kills': kills
}

# Create data frame
try:
    df = pd.DataFrame(player_info)
    print(df)
    df.to_csv('extracted_text/' + 'game2/' + img_name + '.csv', index=True, index_label="index")
except:
    print('Player and kills must have the same length')


plt.imshow(img)
plt.show()