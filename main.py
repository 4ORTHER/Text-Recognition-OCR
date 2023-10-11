from text_extraction import TextExtraction

path_folder = r'images/DOW-mini-tour-30/Game1/'
destination_folder = r'results/Game1/'

text_extraction = TextExtraction()
text_extraction.extract_text(path_folder, destination_folder)