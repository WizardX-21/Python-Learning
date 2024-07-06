from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()
print(contents.replace('I','We'))