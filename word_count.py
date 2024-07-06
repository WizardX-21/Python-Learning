from pathlib import Path

def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        #print(f"Sorry, the file {path} does not exist.")
        pass
    else:
        # Count the approximate number of words in the file
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

# List of filenames in the 'Txt files' folder
filenames = ['Romeo_juliet.txt', 'Room.txt', 'The_Blue_Castle.txt', 'The_Enchanted.txt']
folder = Path('Txt files')

# Loop to count words in each file
for filename in filenames:
    path = folder / filename
    count_words(path)
